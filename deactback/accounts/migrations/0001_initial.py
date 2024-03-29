# Generated by Django 4.2.11 on 2024-03-27 17:45

from django.db import migrations, models
import siwe_auth.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('ethereum_address', models.CharField(max_length=42, primary_key=True, serialize=False, unique=True, validators=[siwe_auth.models.validate_ethereum_address])),
                ('ens_name', models.CharField(blank=True, max_length=255, null=True)),
                ('ens_avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='datetime created')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=264, unique=True)),
                ('name', models.CharField(blank=True, max_length=264, null=True)),
                ('account_type', models.CharField(choices=[('ind', 'Individual'), ('company', 'Company/Organisation'), ('institution', 'Educational Institution')], default='ind', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
