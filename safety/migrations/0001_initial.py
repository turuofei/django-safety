# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='safety_password_reset', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('reset_required', models.BooleanField(db_index=True, default=False, verbose_name='reset required')),
                ('last_reset', models.DateTimeField(verbose_name='last reset')),
            ],
            options={
                'verbose_name': 'password reset',
                'verbose_name_plural': 'password resets',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40, verbose_name='session key')),
                ('ip', models.GenericIPAddressField(verbose_name='IP')),
                ('user_agent', models.CharField(max_length=200, verbose_name='user agent')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('device', models.CharField(blank=True, max_length=200, null=True, verbose_name='device')),
                ('expiration_date', models.DateTimeField(db_index=True, verbose_name='expiration date')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='last activity')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
            },
        ),
        migrations.AlterIndexTogether(
            name='passwordreset',
            index_together=set([('reset_required', 'last_reset')]),
        ),
    ]
