from django.shortcuts import render
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


# Login With Google
class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "postmessage"
    client_class = OAuth2Client


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.EMAIL_FIELD

    def validate(self, attrs):
        # Manually authenticate the user with email and password
        self.user = authenticate(
            request=self.context.get("request"),
            username=attrs.get("email"),  # replace 'username' with 'email'
            password=attrs.get("password"),
        )

        if self.user is None:
            raise serializers.ValidationError({"detail": "Invalid credentials"})

        if not self.user.is_active:
            raise serializers.ValidationError({"detail": "User account is disabled"})

        refresh = self.get_token(self.user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "pk": self.user.pk,
                "username": self.user.username,
                "email": self.user.email,
                "first_name": self.user.first_name,
                "last_name": self.user.last_name,
                "is_rescuer": self.user.is_rescuer,
                "is_affected": self.user.is_affected,
                "is_health_shelter": self.user.is_health_shelter,
            },
        }

        return data
