from django.contrib import admin

from apps.account.models import DiscordUser


@admin.register(DiscordUser)
class DiscordUserAdmin(admin.ModelAdmin):
    """
    Register DiscordUser model to admin site.
    """

    list_display = (
        "id",
        "discord_tag",
        "public_flags",
        "flags",
        "avatar",
        "locale",
        "mfa_enabled",
        "last_login",
    )
