# Generated by Django 2.0.13 on 2019-07-16 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layer2', '0003_auto_20190716_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='status',
            field=models.CharField(choices=[('up', 'UP'), ('down', 'DOWN')], max_length=5),
        ),
    ]
