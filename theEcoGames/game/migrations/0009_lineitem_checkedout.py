# Generated by Django 4.1.1 on 2023-04-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_rename_recordedtime_lineitem_daterecorded'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineitem',
            name='checkedOut',
            field=models.BooleanField(default=False),
        ),
    ]