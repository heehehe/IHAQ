# Generated by Django 2.0.1 on 2018-11-04 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0012_auto_20181104_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatnode',
            name='user_id',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='chatnode',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 19, 29, 22, 401439)),
        ),
        migrations.AlterField(
            model_name='chatnode',
            name='ddabong',
            field=models.IntegerField(default=0),
        ),
    ]
