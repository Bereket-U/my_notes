# Generated by Django 3.2.9 on 2022-03-31 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 31, 17, 28, 33, 761972)),
        ),
    ]