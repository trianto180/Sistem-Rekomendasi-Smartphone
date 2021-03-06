# Generated by Django 2.2.12 on 2021-02-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('cpu_spek', models.CharField(max_length=255)),
                ('gpu', models.CharField(max_length=255)),
                ('storage', models.CharField(max_length=255)),
                ('storage_rem', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=255)),
                ('launcher', models.CharField(max_length=255)),
                ('dimension', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('battery', models.CharField(max_length=255)),
                ('recharge', models.CharField(max_length=255)),
                ('display', models.CharField(max_length=255)),
                ('camera', models.CharField(max_length=255)),
                ('fingerprint', models.CharField(max_length=255)),
                ('facial', models.CharField(max_length=255)),
            ],
        ),
    ]
