# Generated by Django 2.2.12 on 2021-03-21 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rekomendasi', '0011_smartphone_recomm_smartphone_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone_recomm',
            old_name='Smartphone_id',
            new_name='smartphone',
        ),
    ]
