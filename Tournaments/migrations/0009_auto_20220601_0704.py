# Generated by Django 3.2.13 on 2022-06-01 01:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournaments', '0008_auto_20220531_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='tournaments/'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='team_size',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]