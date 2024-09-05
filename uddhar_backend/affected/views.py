from rest_framework.views import APIView
from rest_framework.response import Response
from utils.send_emails import notify

# serializers
from affected.serializers import AffectedRequestSerializer

# models
from affected.models import AffectedRequest, AffectedUser


class AffectedUserView(APIView):
    def put(self, request, format=None, *args, **kwargs):
        if request.user and request.user.is_authenticated and request.user.is_affected:
            user = request.user.affected_user
            user.name = request.data.get("name", user.name)
            user.address = request.data.get("address", user.address)
            user.latitude = request.data.get("latitude", user.latitude)
            user.longitude = request.data.get("longitude", user.longitude)
            user.contact_number = request.data.get(
                "contact_number", user.contact_number
            )
            user.alternative_contact_number = request.data.get(
                "alternative_contact_number", user.alternative_contact_number
            )
            user.blood_group = request.data.get("blood_group", user.blood_group)
            user.save()
            return Response(
                {
                    "status": "User updated successfully.",
                    "data": {
                        "name": user.name,
                        "address": user.address,
                        "latitude": user.latitude,
                        "longitude": user.longitude,
                        "contact_number": user.contact_number,
                        "alternative_contact_number": user.alternative_contact_number,
                        "blood_group": user.blood_group,
                    },
                }
            )
        return Response({"error": "User has to be logged in to view affected user."})

    def get(self, request, format=None, *args, **kwargs):
        if request.user and request.user.is_authenticated and request.user.is_affected:
            user = request.user.affected_user
            return Response(
                {
                    "name": user.name,
                    "address": user.address,
                    "latitude": user.latitude,
                    "longitude": user.longitude,
                    "contact_number": user.contact_number,
                    "alternative_contact_number": user.alternative_contact_number,
                    "blood_group": user.blood_group,
                }
            )
        return Response({"error": "User has to be logged in to view affected user."})


class AffectedRequestView(APIView):
    serializer_class = AffectedRequestSerializer

    def post(self, request, format=None, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if (
                request.user
                and request.user.is_authenticated
                and request.user.is_affected
            ):
                affected_instance = serializer.save(user=request.user.affected_user)

            affected_instance = serializer.save()

            # send email
            notify(affected=affected_instance)

            return Response(
                {"status": "Request created successfully.", "data": serializer.data}
            )
        return Response(serializer.errors)

    def get(self, request, format=None, *args, **kwargs):
        if request.GET.get("all") == "true":
            requests = AffectedRequest.objects.all().order_by("-requested_on")
            serializer = self.serializer_class(requests, many=True)
            return Response(serializer.data)

        if request.user and request.user.is_authenticated and request.user.is_affected:
            requests = AffectedRequest.objects.filter(user=request.user.affected_user)
            serializer = self.serializer_class(requests, many=True)
            return Response(serializer.data)

        return Response({"error": "User has to be logged in to view requests."})


class getCount(APIView):
    def get(self, request):
        count = AffectedUser.objects.all().count()
        help_seeked = AffectedRequest.objects.all().count()
        helped = AffectedRequest.objects.filter(status="completed").count()

        return Response(
            {
                "help_seeked": help_seeked,
                "helped": helped,
                "total_user": count,
            }
        )
