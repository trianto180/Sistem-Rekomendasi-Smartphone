# Generated by Django 2.2.12 on 2021-03-11 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekomendasi', '0005_auto_20210312_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='smartphone_recomm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smartphone_name', models.CharField(max_length=256)),
                ('cos_sim', models.FloatField()),
            ],
        ),
    ]
