from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.forms import ValidationError

# Create your views here.
from .forms import RegisterForm
from .models import Register
from Tournaments.models import Tournament

@login_required
def register_checkout_view(request, pk):
    try:
        tournament = Tournament.objects.get(pk=pk)
    except:
        raise Http404

    form = RegisterForm(request.POST or None, tournament=tournament, user=request.user)
    print(form.data)
    print(form.errors)
    if form.is_valid():
        print(form.cleaned_data)
        membersNameString = ''
        if(tournament.team_size<2):
            membersNameString = form.cleaned_data.get("team_name")
        else:
            for i in range(tournament.team_size):
                membersNameString += str(form.data.get('ign'+str(i+1))) + ', \n'
        
        obj = form.save(commit=False)
        user = request.user
        obj.Tournament = tournament
        obj.team_name = form.cleaned_data.get("team_name")
        obj.team_members = membersNameString
        obj.user = user
        
        obj.mark_registered(save=False)
        obj.save()

        return redirect(f"/tournament/{tournament.id}")
        
    return render(request, 'registerations/register.html', {"form":form, "tournament":tournament}) 

@staff_member_required
def tournament_registerations_view(request, pk):
    pk=pk
    try:
        qs = Register.objects.filter(Tournament__id = pk)
    except:
        raise Http404
    
    
    context = {'obj_list':qs}
    return render(request, 'table.html', context)


