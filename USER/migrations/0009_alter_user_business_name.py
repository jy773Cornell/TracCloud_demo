# Generated by Django 4.1.5 on 2023-01-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0008_alter_userrelation_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='business_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Business Name'),
        ),
    ]