# Generated by Django 3.2.13 on 2022-05-22 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registerations', '0002_rename_product_register_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='ign',
            field=models.CharField(default='00', max_length=20, unique=True),
        ),
    ]