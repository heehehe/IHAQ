# Generated by Django 2.0.1 on 2018-11-04 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0010_auto_20181104_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 17, 16, 11, 879135)),
        ),
        migrations.AlterField(
            model_name='chat',
            name='ddabong',
            field=models.IntegerField(default=1),
        ),
    ]
