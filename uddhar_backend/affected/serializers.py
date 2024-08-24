from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from affected.models import AffectedUser, AffectedRequest


class AffectedUserProfile(serializers.ModelSerializer):
    class Meta:
        model = AffectedUser
        exclude = ("user", "status")


class AffectedRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffectedRequest
        exclude = (
            "status",
            "rescuer_positions",
            "rescuer_descriptions",
            "rescue_updated_times",
            "rescue_active_from",
        )
