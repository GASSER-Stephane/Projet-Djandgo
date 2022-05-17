# Generated by Django 4.0.4 on 2022-05-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mideles', models.CharField(max_length=100)),
                ('marques', models.CharField(max_length=100)),
                ('prix', models.IntegerField()),
                ('poids', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ListeEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prixmoyen', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
