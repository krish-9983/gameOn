
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['firstname','lastname', 'phone', 'bio', 'country',]

        widgets = {
            'firstname': forms.TextInput(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control', 'rows':"3",}),

            'lastname' : forms.TextInput(attrs={'class':'form-control'}),

            'country':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),

        }



