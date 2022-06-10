from datetime import datetime
import imp
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import (CreateView)
from .forms import TournamentCreateForm
from django.db.models import Q
from registerations.models import Register

from .models import Tournament

# Create your views here.
def tournaments_view(request, *args, **kwargs):
    qs = Tournament.objects.filter(tournament_date__gte = datetime.today())
    context = {"object_list" : qs,}
    return render(request, "tournaments.html", context)

def tournament_detail_view(request, pk):
    try:
        obj = Tournament.objects.get(pk=pk)
        qs = Register.objects.filter(Tournament__id=pk).filter(user__username=request.user)
        participation_status = False
        register_details = []
        if qs.exists():
            participation_status = True
            register_details = qs[0]
    except:
        raise Http404
    return render(request, "tournaments/details.html", {"object":obj,"participation_status":participation_status,"registered":register_details,})

def search_view(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        objs = Tournament.objects.filter(Q(tournament_date__gte = datetime.today()) & (Q(game__contains=searched) | Q(title__contains=searched)))
        return render(request, 'tournaments.html', {'object_list':objs})
    else:
        return render(request, 'home.html')


@staff_member_required
def tournament_create_view(request):
    form = TournamentCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print('form is valid')
        object = form.save(commit=False)
        object.title = form.cleaned_data.get('title')
        object.content = form.cleaned_data.get('content')
        object.last_date = form.cleaned_data.get('last_date')
        object.tournament_date = form.cleaned_data.get('tournament_date')
        object.game = form.cleaned_data.get('game')
        object.team_size = form.cleaned_data.get('team_size')
        object.prize_pool = form.cleaned_data.get('prize_pool')
        object.prize1 = form.cleaned_data.get('prize1')
        object.prize2 = form.cleaned_data.get('prize2')
        object.prize3 = form.cleaned_data.get('prize3')
        object.winner = form.cleaned_data.get('winner')
        image = request.FILES.get('image')
        object.image = image
        object.save()
        object.changeImageSize()
        return redirect(f'/tournament/{object.id}')
    context = {'form':form, 'buttonTitle': 'Create',}
    return render(request, 'tournament_Create_Form.html', context)

@staff_member_required
def tournament_delete_view(request, pk):
    try:
        obj = Tournament.objects.filter(pk=pk).delete()

    except:
        raise Http404
    return redirect('/home')

