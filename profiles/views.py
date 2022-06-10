import imp
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from .forms import ProfileEditForm
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy

from registerations.models import Register

# Create your views here.
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user':user})

@login_required
def profile_edit_view(request):
    form = ProfileEditForm(request.POST or None, instance=request.user.profile)
    if form.is_valid():
        object = form.save(commit=False)
        object.firstname = form.cleaned_data.get("firstname")
        object.lastname = form.cleaned_data.get("lastname")
        object.bio = form.cleaned_data.get("bio")
        object.phone = form.cleaned_data.get("phone")
        object.country = form.cleaned_data.get("country")

        object.save()
        return redirect('/accounts/profile/')

    return render(request, 'profile_edit.html', {"form":form}) 

@login_required
def profile_tournament_history_view(request):
    qs = Register.objects.filter(user__username = request.user.username)
    context = {'obj_list':qs}
    return render(request, 'table.html', context)