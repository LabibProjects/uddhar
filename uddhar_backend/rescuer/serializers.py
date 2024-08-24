from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from rescuer.models import RescuerUser
from affected.models import AffectedRequest


class RescuerUserRegistrationSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    name = serializers.CharField(max_length=200, required=False)
    address = serializers.CharField(max_length=400, required=False)
    contact_number = serializers.CharField(max_length=200, required=False)
    category = serializers.ListField(
        child=serializers.CharField(max_length=200), required=False
    )

    def get_cleaned_data(self):
        data = super(RescuerUserRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            "name": self.validated_data.get("name", ""),
            "address": self.validated_data.get("address", ""),
            "contact_number": self.validated_data.get("contact_number", ""),
            "category": self.validated_data.get("category", []),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(RescuerUserRegistrationSerializer, self).save(request)
        user.is_rescuer = True
        user.save()

        rescuer = RescuerUser(
            user=user,
            name=self.validated_data.get("name", ""),
            address=self.validated_data.get("address", ""),
            contact_number=self.validated_data.get("contact_number", ""),
            category=self.validated_data.get("category", []),
        )
        rescuer.save()
        return user


class AffectedRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffectedRequest
        fields = "__all__"


class AffectedRequestUpdateSerializer(serializers.Serializer):
    STATUS = (
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    )
    status = serializers.ChoiceField(choices=AffectedRequest.STATUS, required=True)
    rescuer_latitude = serializers.FloatField(required=True)
    rescuer_longitude = serializers.FloatField(required=True)
    rescuer_description = serializers.CharField(max_length=500, required=False)
