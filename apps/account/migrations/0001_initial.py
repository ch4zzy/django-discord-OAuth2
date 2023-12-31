# Generated by Django 4.2 on 2023-07-01 10:37

import apps.account.managers
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
            name='DiscordUser',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('discord_tag', models.CharField(max_length=255)),
                ('public_flags', models.IntegerField()),
                ('flags', models.IntegerField()),
                ('avatar', models.CharField(max_length=255)),
                ('locale', models.CharField(max_length=255)),
                ('mfa_enabled', models.BooleanField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('objects', apps.account.managers.DiscordUserOAuth2Manager()),
            ],
        ),
    ]
