# Generated by Django 4.1.5 on 2023-01-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0005_alter_usertype_typename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='TypeName',
            field=models.CharField(max_length=128, unique=True, verbose_name='Type Name'),
        ),
    ]