# Generated by Django 3.1.2 on 2020-10-13 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapi', '0002_users_ass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='ass',
        ),
    ]
