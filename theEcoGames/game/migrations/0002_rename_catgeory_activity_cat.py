# Generated by Django 4.1.1 on 2023-04-03 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='catgeory',
            new_name='cat',
        ),
    ]