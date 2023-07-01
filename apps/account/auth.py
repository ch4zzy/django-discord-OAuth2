from django.contrib.auth.backends import BaseBackend

from apps.account.models import DiscordUser


class DiscordBackend(BaseBackend):
    def authenticate(self, request, user):
        check_user = DiscordUser.objects.filter(id=user["id"])
        if not check_user.exists():
            new_user = DiscordUser.objects.create_new_discord_user(user)
            return new_user
        return check_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(pk=user_id)
        except DiscordUser.DoesNotExist:
            return None
