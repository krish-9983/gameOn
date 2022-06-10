
from django import forms

from .models import Register

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        tournament = kwargs.pop("tournament") or None
        user = kwargs.pop("user") or None
        super().__init__(*args, **kwargs)
        self.user = user
        self.tournament = tournament

    class Meta:
        model = Register
        fields = [
            'team_name',
        ]

    def clean_team_name(self):
        team_name = self.cleaned_data.get('team_name')
        qs = Register.objects.filter(Tournament__id = self.tournament.id).filter(team_name__contains=team_name)
        if qs.exists():
            raise forms.ValidationError("This Name is already registered")
        return team_name

        
    def user_check(self, *args, **kwargs):
        qs = Register.objects.filter(Tournament__id = self.tournament.id).filter(user__username=self.user)
        if qs.exists():
            return True
        return False

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)

        if self.user_check(self):
            raise forms.ValidationError("You are Already Registered.")

        if self.tournament != None:
            if not self.tournament.has_entryleft():
                raise forms.ValidationError("Entries Full")
            return cleaned_data