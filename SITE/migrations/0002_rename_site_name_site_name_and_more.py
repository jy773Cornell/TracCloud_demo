# Generated by Django 4.1.5 on 2023-01-22 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SITE', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='site_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='site_variety',
            new_name='variety',
        ),
        migrations.RenameField(
            model_name='sitetype',
            old_name='type_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sitevariety',
            old_name='variety_name',
            new_name='name',
        ),
    ]
