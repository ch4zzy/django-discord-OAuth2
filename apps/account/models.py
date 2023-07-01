from django.contrib.auth.models import User
from django.db import models

from apps.account.managers import DiscordUserOAuth2Manager


class DiscordUser(models.Model):
    """
    Profile model for storing Discord OAuth2 data.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    objects = DiscordUserOAuth2Manager()
    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=255)
    public_flags = models.IntegerField()
    flags = models.IntegerField()
    avatar = models.CharField(max_length=255)
    locale = models.CharField(max_length=255)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True, blank=True)

    def is_authenticated(self, request):
        return True
