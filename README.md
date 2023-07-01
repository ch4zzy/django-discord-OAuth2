# django-discord-OAuth2
This Django project includes an implementation of OAuth2 authentication with Discord and a custom model called DiscordUser to store Discord OAuth2 data.

## DiscordUser Model
The DiscordUser model represents a user profile and stores Discord OAuth2 data. It has the following fields:


**user:** A one-to-one relationship with the built-in User model from django.contrib.auth.models, which is used to associate the Discord user with a Django user.

**id:** A BigIntegerField serving as the primary key for the Discord user.

**discord_tag:** A CharField representing the Discord username.

**public_flags:** An IntegerField storing the public flags associated with the Discord user.

**flags:** An IntegerField storing the flags associated with the Discord user.

**avatar:** A CharField representing the avatar URL of the Discord user.

**locale:** A CharField storing the locale of the Discord user.

**mfa_enabled:** A BooleanField indicating whether the Discord user has two-factor authentication enabled.

**last_login:** A DateTimeField representing the last login date and time of the Discord user.

The DiscordUser model also includes a custom manager called DiscordUserOAuth2Manager. This manager provides a method **create_new_discord_user()** to create a new DiscordUser instance associated with a Django User instance.


## DiscordBackend
The DiscordBackend class is a custom authentication backend that extends django.contrib.auth.backends.BaseBackend. It provides the **authenticate()** and **get_user()** methods required for the authentication process.

In the **authenticate()** method, the Discord user data is passed as the user parameter. It checks if a DiscordUser instance with the same Discord ID already exists. If not, a new DiscordUser instance is created using the **create_new_discord_user()** method of the DiscordUserOAuth2Manager. The new user is then returned.

The **get_user()** method is implemented to retrieve a DiscordUser instance based on the user ID.

These components work together to enable OAuth2 authentication with Discord and store the associated user data in the DiscordUser model.

## URL Patterns
The urlpatterns list defines the URL patterns for the OAuth2 authentication process with Discord. It includes the following paths:

```/auth/```: The endpoint for retrieving the authenticated user data. It maps to the get_authenticated_user view.

```/oauth2/login/```: The endpoint for initiating the Discord OAuth2 login flow. It redirects the user to the Discord authorization URL. This URL is handled by the discord_login view.

```/oauth2/login/redirect/```: The redirect endpoint after the user authorizes the Discord login. It exchanges the authorization code for an access token and retrieves the user data. This URL is handled by the discord_login_redirect view.

## Configuration
Environment Configuration
Configure the necessary environment variables in a **.env** file. Make sure to set the following variables:

**SECRET_KEY:** The secret key used for Django.

**DEBUG:** Set to True for development mode.

Discord OAuth2 Configuration:

**auth_url_discord:** The Discord authorization URL.

**client_id:** Your Discord application client ID.

**client_secret:** Your Discord application client secret.

**redirect_uri:** The redirect URI for Discord OAuth2.

**token_url:** The Discord token URL.

**user_url:** The Discord user URL.

## Usage

Follow the registration and login processes as described in the previous sections. The OAuth2 flow will utilize the Discord authentication provider for user registration and login.

## Contributing

Contributions are welcome! If you find any issues or would like to add new features, feel free to open a pull request.
