# Generated by Django 2.0.5 on 2019-04-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='datein',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dateout',
            field=models.CharField(max_length=20),
        ),
    ]
