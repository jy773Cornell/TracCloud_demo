# Generated by Django 4.1.5 on 2023-01-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0003_alter_usertype_infodatatable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='UUID',
            new_name='UID',
        ),
        migrations.RenameField(
            model_name='usertype',
            old_name='UUID',
            new_name='UTID',
        ),
        migrations.AlterField(
            model_name='user',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='Delete Status'),
        ),
        migrations.AlterField(
            model_name='usertype',
            name='isDelete',
            field=models.BooleanField(default=False, verbose_name='Delete Status'),
        ),
    ]
