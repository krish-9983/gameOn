
from PIL import Image
from distutils.command.upload import upload
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import datetime
# Create your models here.

class Tournament(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='tournaments/', null=True, blank=True)
    content = models.TextField(null = True, blank= True)
    last_date = models.DateField( default=datetime.date.today)
    tournament_date = models.DateField( default=datetime.date.today)
    game = models.CharField(max_length=50, null = True)
    team_size = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    prize_pool = models.PositiveIntegerField(default=0)
    entryleft = models.PositiveIntegerField(default=0)
    prize1 = models.CharField(max_length=20, default='0', null=True)
    prize2 = models.CharField(max_length=20, default='0', null=True)
    prize3 = models.CharField(max_length=20, default='0', null=True)
    winner = models.CharField(max_length=30 ,default='', null=True, blank=True)

    def has_entryleft(self):
        return self.entryleft > 0

    def entry_full(self, count=1, save=True):
        current_entry = self.entryleft
        current_entry -= count
        self.entryleft = current_entry
        if save==True:
            self.save()
        return self.entryleft


    def __unicode__(self):
        return "{0}".format(self.image)

    def changeImageSize(self):
        if not self.image:
            return            

        image = Image.open(self.image)
        (width, height) = image.size     
        size = ( 2000, 1000)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)
