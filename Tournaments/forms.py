from django import forms

from .models import Tournament

class DateInput(forms.DateInput):
    input_type: 'date'

class TournamentCreateForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['title', 'content', 'tournament_date', 'game', 'team_size', 'prize_pool', 'entryleft', 'prize1', 'prize2', 'prize3', 'winner','image','last_date',]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'rows':"3",}),
            'tournament_date' : forms.DateInput(attrs={'class':'form-control',}),
            'game' : forms.TextInput(attrs={'class':'form-control'}), 
            'team_size':forms.NumberInput(attrs={'class':'form-control'}), 
            'prize_pool':forms.NumberInput(attrs={'class':'form-control'}), 
            'entryleft': forms.NumberInput(attrs={'class':'form-control'}), 
            'prize1':forms.TextInput(attrs={'class':'form-control'}), 
            'prize2':forms.TextInput(attrs={'class':'form-control'}), 
            'prize3':forms.TextInput(attrs={'class':'form-control'}), 
            'winner':forms.TextInput(attrs={'class':'form-control'}), 
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'last_date':forms.DateInput(attrs={'class':'form-control',}),

        }