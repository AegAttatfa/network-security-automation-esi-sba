# Generated by Django 2.0.13 on 2019-07-12 13:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(199)])),
                ('sourceIP', models.GenericIPAddressField(protocol='IPv4')),
                ('destinationIP', models.GenericIPAddressField(protocol='IPv4')),
                ('protocol', models.CharField(choices=[('TCP', 'TCP'), ('UDP', 'UDP'), ('ICMP', 'ICMP')], max_length=6)),
            ],
        ),
    ]
