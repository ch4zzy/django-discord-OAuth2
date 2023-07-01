from django.urls import path

from apps.account.views import (
    discord_login,
    discord_login_redirect,
    get_authenticated_user,
)

urlpatterns = [
    path("auth/", get_authenticated_user, name="get_authenticated_user"),
    path("oauth2/login/", discord_login, name="oauth2_login"),
    path("oauth2/login/redirect/", discord_login_redirect, name="oauth2_login_redirect"),
]
