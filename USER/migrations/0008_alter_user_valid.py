# Generated by Django 4.1.5 on 2023-01-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0007_remove_user_isdelete_remove_usertype_isdelete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Valid',
            field=models.BooleanField(default=False, verbose_name='Valid Status'),
        ),
    ]
