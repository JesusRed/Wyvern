# Generated by Django 3.1.5 on 2021-01-21 16:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WyvernPosters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='calificacion',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]