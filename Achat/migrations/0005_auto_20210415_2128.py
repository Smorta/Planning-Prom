# Generated by Django 3.1.4 on 2021-04-15 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Achat', '0004_auto_20210415_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chantier',
            old_name='id_Gestionnaire',
            new_name='id_Responsable',
        ),
    ]