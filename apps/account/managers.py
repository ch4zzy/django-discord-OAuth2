from django.contrib.auth import models
from datetime import datetime
from django.contrib.auth.models import User


class DiscordUserOAuth2Manager(models.UserManager):
    """
    Create a new DiscordUser instance associated with a User instance.
    """
    
    def create_new_discord_user(self, user_data):
        user = User.objects.create_user(username=user_data["username"])
        new_user = self.create(
            user=user,
            id=user_data["id"],
            discord_tag=user_data["username"],
            avatar=user_data["avatar"],
            public_flags=user_data["public_flags"],
            flags=user_data["flags"],
            locale=user_data["locale"],
            mfa_enabled=user_data["mfa_enabled"],
            last_login=datetime.now(),
        )
        return new_user
