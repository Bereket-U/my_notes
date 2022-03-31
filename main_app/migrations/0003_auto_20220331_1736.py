# Generated by Django 3.2.9 on 2022-03-31 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20220331_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 31, 17, 35, 54, 362440)),
        ),
    ]
