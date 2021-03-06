# Generated by Django 3.1.5 on 2021-01-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('sinopsis', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to='')),
                ('calificacion', models.DecimalField(decimal_places=1, max_digits=2)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'poster',
                'verbose_name_plural': 'posters',
            },
        ),
    ]
