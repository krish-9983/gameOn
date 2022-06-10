from django.db import models
from django.contrib.auth import get_user_model

from Tournaments.models import Tournament

# Create your models here.

User = get_user_model()

REGISTER_STATUS_CHOICES = (
    ('00', 'Registered'),
    ('01', 'Not Registered'),
)

class Register(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Tournament = models.ForeignKey(Tournament, null=True, on_delete=models.SET_NULL)
    team_name = models.CharField(max_length=20, default='00')
    team_members = models.TextField(default=' ')
    status = models.CharField(max_length=20, choices=REGISTER_STATUS_CHOICES, default='01')
    entryleft_updated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def mark_registered(self, save=False):
        self.status = '00'
        if not self.entryleft_updated and self.Tournament:
            self.Tournament.entry_full(save=True)
            self.entryleft_updated = True
        if save == True:
            self.save()

        return self.status
             
