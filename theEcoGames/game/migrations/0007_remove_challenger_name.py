# Generated by Django 4.1.1 on 2023-03-25 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_challenger_delete_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenger',
            name='name',
        ),
    ]
