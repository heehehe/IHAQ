# Generated by Django 2.0.1 on 2018-11-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0017_auto_20181107_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classnode',
            old_name='class_id',
            new_name='class_name',
        ),
        migrations.AlterField(
            model_name='chatnode',
            name='created_date',
            field=models.CharField(default='2018-11-07 18:17:25', max_length=50),
        ),
    ]
