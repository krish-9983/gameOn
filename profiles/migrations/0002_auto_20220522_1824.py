# Generated by Django 3.2.13 on 2022-05-22 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='content',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
