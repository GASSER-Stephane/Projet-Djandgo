# Generated by Django 4.0.4 on 2022-05-09 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livre', '0002_biblio'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='bibliotheque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livre.biblio'),
        ),
    ]