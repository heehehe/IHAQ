# Generated by Django 2.0.1 on 2018-11-04 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_auto_20181104_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_unique_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 17, 10, 29, 227159)),
        ),
    ]
