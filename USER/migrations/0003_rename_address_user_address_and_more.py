# Generated by Django 4.1.5 on 2023-01-19 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USER', '0002_user_create_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='BusinessName',
            new_name='business_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Cell',
            new_name='cell',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='County',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='RegExpireDate',
            new_name='reg_expire_date',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='RegistrationNo',
            new_name='registration_no',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='State',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='UID',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Username',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Zipcode',
            new_name='zipcode',
        ),
        migrations.RemoveField(
            model_name='user',
            name='AddedBy',
        ),
        migrations.RemoveField(
            model_name='user',
            name='SelfActivated',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Valid',
        ),
        migrations.AddField(
            model_name='user',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_added_by', to='USER.user', verbose_name='Added By'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active'),
        ),
        migrations.AddField(
            model_name='user',
            name='self_activated',
            field=models.BooleanField(default=True, verbose_name='Self Activated'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_type', to='USER.usertype', verbose_name='User Type'),
        ),
    ]
