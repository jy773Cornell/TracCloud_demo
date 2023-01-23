# Generated by Django 4.1.5 on 2023-01-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SITE', '0003_sitetype_parent_type_alter_site_owner_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetype',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Type Name'),
        ),
        migrations.AlterField(
            model_name='siteunit',
            name='unit',
            field=models.CharField(max_length=32, unique=True, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='sitevariety',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Variety Name'),
        ),
    ]
