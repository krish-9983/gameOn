# Generated by Django 3.2.13 on 2022-05-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerations', '0004_auto_20220522_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='ign',
        ),
        migrations.AddField(
            model_name='register',
            name='team_members',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='register',
            name='team_name',
            field=models.CharField(default='00', max_length=20),
        ),
    ]
