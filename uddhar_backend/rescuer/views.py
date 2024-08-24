from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from dj_rest_auth.registration.views import RegisterView
from rescuer.serializers import (
    RescuerUserRegistrationSerializer,
    AffectedRequestSerializer,
    AffectedRequestUpdateSerializer,
)
from affected.models import AffectedRequest
from django.utils.timezone import datetime


class RescuerRegistrationView(RegisterView):
    serializer_class = RescuerUserRegistrationSerializer


class AffectedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id=None, format=None, *args, **kwargs):
        rescuer = request.user.rescuer_user
        if user_id:
            requests = AffectedRequest.objects.get(id=user_id, rescuer_user=rescuer)
            serializer = AffectedRequestSerializer(requests)
            return Response(serializer.data)
        else:
            requests = AffectedRequest.objects.filter(rescuer_user=rescuer).order_by(
                "-requested_on"
            )
            serializer = AffectedRequestSerializer(requests, many=True)
            return Response(serializer.data)

    def put(self, request, user_id=None, format=None, *args, **kwargs):
        if user_id is None:
            return Response({"error": "User ID is required"}, status=400)

        rescuer = request.user.rescuer_user
        serializer = AffectedRequestUpdateSerializer(data=request.data)
        affected_request = AffectedRequest.objects.get(id=user_id, rescuer_user=rescuer)

        if serializer.is_valid():
            affected_request.status = serializer.validated_data.get("status")
            affected_request.rescuer_positions.append(
                {
                    "latitude": serializer.validated_data.get("rescuer_latitude"),
                    "longitude": serializer.validated_data.get("rescuer_longitude"),
                }
            )
            affected_request.rescuer_descriptions.append(
                serializer.validated_data.get("rescuer_description", "")
            )
            affected_request.rescue_updated_times.append(datetime.now())
            affected_request.save()

            return Response(
                {
                    "status": "success",
                    "data": serializer.data,
                }
            )

        return Response(serializer.errors)
