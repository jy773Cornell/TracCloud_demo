# Generated by Django 4.1.5 on 2023-01-23 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SITE', '0002_rename_site_name_site_name_and_more'),
        ('CHEMICAL', '0001_initial'),
        ('USER', '0013_rename_type_name_userrelationtype_name_and_more'),
        ('CROP', '0003_rename_crop_name_crop_name_and_more'),
        ('OPERATION', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationPurpose',
            fields=[
                ('apid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='APID')),
                ('name', models.CharField(max_length=128, verbose_name='Type Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('atid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='ATID')),
                ('name', models.CharField(max_length=128, verbose_name='Type Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='DecisionSupport',
            fields=[
                ('dsid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='DSID')),
                ('name', models.CharField(max_length=128, verbose_name='Type Name')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRecord',
            fields=[
                ('prid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='PRID')),
                ('pur_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Purchase Datetime')),
                ('vendor', models.CharField(blank=True, max_length=128, null=True, verbose_name='Vendor')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('cost_per_unit', models.FloatField(verbose_name='Cost Per Unit')),
                ('total_cost', models.FloatField(verbose_name='Total Cost')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('chemical', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pr_chem', to='CHEMICAL.chemical', verbose_name='Chemical')),
                ('chemical_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pr_chem_type', to='CHEMICAL.chemicaltype', verbose_name='Chemical Type')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pr_op_user', to='USER.user', verbose_name='Operator')),
                ('opid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pr_op', to='OPERATION.operation', verbose_name='OPID')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pr_user', to='USER.user', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='HarvestRecord',
            fields=[
                ('hrid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='HRID')),
                ('har_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Harvest Datetime')),
                ('planting_date', models.DateField(blank=True, null=True, verbose_name='Planting Date')),
                ('bloom_date', models.DateField(blank=True, null=True, verbose_name='Bloom Date')),
                ('hr_area', models.FloatField(verbose_name='Harvest Area')),
                ('rows', models.IntegerField(verbose_name='Rows')),
                ('tracing_no', models.CharField(blank=True, max_length=128, null=True, verbose_name='Tracking No.')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('area_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_opu', to='OPERATION.operationunit', verbose_name='Area Unit')),
                ('crop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_crop', to='CROP.crop', verbose_name='Crop')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_op_user', to='USER.user', verbose_name='Operator')),
                ('opid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_op', to='OPERATION.operation', verbose_name='OPID')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_site', to='SITE.site', verbose_name='Site')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hr_user', to='USER.user', verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationRecord',
            fields=[
                ('arid', models.CharField(max_length=48, primary_key=True, serialize=False, verbose_name='ARID')),
                ('app_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Harvest Datetime')),
                ('water_use', models.BooleanField(verbose_name='Water Use')),
                ('application_rate', models.FloatField(verbose_name='Application Rate')),
                ('total_amount', models.FloatField(verbose_name='Total Amount')),
                ('total_cost', models.FloatField(verbose_name='Total Cost')),
                ('applied_area', models.FloatField(verbose_name='Applied Area')),
                ('decide_by', models.CharField(blank=True, max_length=64, null=True, verbose_name='Decided By')),
                ('wind_speed', models.FloatField(blank=True, null=True, verbose_name='Wind Speed')),
                ('wind_direction', models.SmallIntegerField(blank=True, choices=[('1', 'east'), ('2', 'north'), ('3', 'south'), ('4', 'west'), ('5', 'southwest'), ('6', 'northwest'), ('7', 'southeast'), ('8', 'northeast')], null=True, verbose_name='Wind Direction')),
                ('average_temp', models.FloatField(blank=True, null=True, verbose_name='Average Temperature')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='Create Time')),
                ('amount_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_amount_opu', to='OPERATION.operationunit', verbose_name='Amount Unit')),
                ('area_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_area_opu', to='OPERATION.operationunit', verbose_name='Amount Unit')),
                ('chemical', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_chem', to='CHEMICAL.chemical', verbose_name='Chemical')),
                ('chemical_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_chem_type', to='CHEMICAL.chemicaltype', verbose_name='Chemical Type')),
                ('crop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_crop', to='CROP.crop', verbose_name='Crop')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_customer_user', to='USER.user', verbose_name='Customer')),
                ('decision_support', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_decision_support', to='OPERATION.decisionsupport', verbose_name='Decision Support')),
                ('growth_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_growth_stage', to='CROP.cropgrowthstage', verbose_name='Growth Stage')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_op_user', to='USER.user', verbose_name='Operator')),
                ('opid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_op', to='OPERATION.operation', verbose_name='OPID')),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_purpose', to='OPERATION.applicationpurpose', verbose_name='Purpose')),
                ('rate_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_rate_opu', to='OPERATION.operationunit', verbose_name='Rate Unit')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_site', to='SITE.site', verbose_name='Site')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_type', to='OPERATION.applicationtype', verbose_name='Application Type')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_user', to='USER.user', verbose_name='User')),
                ('water_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ar_water_opu', to='OPERATION.operationunit', verbose_name='Water Unit')),
            ],
        ),
    ]