import requests
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect


@login_required(login_url="/oauth2/login")
def get_authenticated_user(request):
    return JsonResponse({"user": "authenticated"})


def discord_login(request):
    """
    Discord OAuth2 login endpoint.
    """

    return redirect(settings.AUTH_URL_DISCORD)


def discord_login_redirect(request):
    """
    Discord OAuth2 redirect endpoint.
    """

    code = request.GET.get("code")
    user_data = exchange_code(code)
    discord_user = authenticate(request, user=user_data)
    login(request, discord_user, backend="apps.account.auth.DiscordBackend")
    return JsonResponse({"user": user_data})


def exchange_code(code):
    """
    Changes the OAuth2 code for a Discord access token.
    """

    data = {
        "client_id": settings.CLIENT_ID,
        "client_secret": settings.CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": settings.REDIRECT_URI,
        "scope": "identify",
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(settings.TOKEN_URL, data=data, headers=headers)
    credentials = response.json()
    access_token = credentials["access_token"]

    response = requests.get(
        settings.USER_URL,
        headers={
            "Authorization": f"Bearer {access_token}",
        },
    )

    user_data = response.json()

    return user_data
