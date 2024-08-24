from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from health_shelter.models import HealthShelterUser, HealthShelterPost


class HealthShelterUserUserRegistrationSerializer(RegisterSerializer):

    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    name = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=400, required=True)
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)
    contact_number = serializers.CharField(max_length=200, required=False)
    alternative_contact_number = serializers.CharField(max_length=200, required=False)

    def get_cleaned_data(self):
        data = super(
            HealthShelterUserUserRegistrationSerializer, self
        ).get_cleaned_data()
        extra_data = {
            "name": self.validated_data.get("name", ""),
            "address": self.validated_data.get("address", ""),
            "latitude": self.validated_data.get("latitude", ""),
            "longitude": self.validated_data.get("longitude", ""),
            "contact_number": self.validated_data.get("contact_number", ""),
            "alternative_contact_number": self.validated_data.get(
                "alternative_contact_number", ""
            ),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(HealthShelterUserUserRegistrationSerializer, self).save(request)
        user.is_health_shelter = True
        user.save()

        health_shelter_user = HealthShelterUser(
            user=user,
            name=self.validated_data.get("name", ""),
            address=self.validated_data.get("address", ""),
            latitude=self.validated_data.get("latitude", ""),
            longitude=self.validated_data.get("longitude", ""),
            contact_number=self.validated_data.get("contact_number", ""),
            alternative_contact_number=self.validated_data.get(
                "alternative_contact_number", ""
            ),
        )
        health_shelter_user.save()
        return user


class HealthShelterPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthShelterPost
        exclude = ("user",)
