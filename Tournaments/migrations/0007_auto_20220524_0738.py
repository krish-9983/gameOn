# Generated by Django 3.2.13 on 2022-05-24 02:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0006_rename_data_tournament_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='date',
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
