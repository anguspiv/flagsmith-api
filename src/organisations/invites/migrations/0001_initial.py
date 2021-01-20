# Generated by Django 2.2.17 on 2021-01-13 21:03

import app.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organisations', '0024_organisation_feature_analytics'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name='Invite',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('hash', models.CharField(default=app.utils.create_hash, max_length=100, unique=True)),
                        ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='DateCreated')),
                        ('frontend_base_url', models.CharField(max_length=500)),
                        ('role', models.CharField(default='USER', max_length=50)),
                        ('email', models.EmailField(max_length=254)),
                        ('invited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_invites', to=settings.AUTH_USER_MODEL)),
                        ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='organisations.Organisation')),
                    ],
                    options={
                        'db_table': 'users_invite',
                        'ordering': ['organisation', 'date_created'],
                        'unique_together': {('email', 'organisation')},
                    },
                ),
            ]
        ),
    ]
