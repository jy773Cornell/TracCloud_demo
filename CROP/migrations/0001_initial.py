# Generated by Django 4.1.5 on 2023-01-24 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('USER', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropCategory',
            fields=[
                ('ccid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='CCID')),
                ('name', models.CharField(max_length=128, verbose_name='Category Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='CropGrowthStage',
            fields=[
                ('cgsid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='CGSID')),
                ('name', models.CharField(max_length=128, verbose_name='Stage Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='CropLifecycle',
            fields=[
                ('clcid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='CLCID')),
                ('name', models.CharField(max_length=128, verbose_name='Lifecycle Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('cid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='CID')),
                ('name', models.SmallIntegerField(choices=[(1, 'Apple'), (2, 'Berry'), (3, 'Cherry'), (4, 'Grape'), (5, 'Pear'), (6, 'Stone Fruit'), (7, 'Golf'), (8, 'Ground'), (9, 'Lawn'), (10, 'Sod')], verbose_name='Crop Name')),
                ('variety_list', models.CharField(max_length=256, verbose_name='Variety List')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_category', to='CROP.cropcategory', verbose_name='Category')),
                ('growth_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_growth_stage', to='CROP.cropgrowthstage', verbose_name='Grow Stage')),
                ('lifecycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_lifecycle', to='CROP.croplifecycle', verbose_name='Lifecycle')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='crop_user', to='USER.user', verbose_name='User')),
            ],
        ),
    ]
