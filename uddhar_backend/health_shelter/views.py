from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.registration.views import RegisterView
from health_shelter.serializers import (
    HealthShelterUserUserRegistrationSerializer,
    HealthShelterPostSerializer,
)

from health_shelter.models import HealthShelterUser, HealthShelterPost


class HealthShelterRegistrationView(RegisterView):
    serializer_class = HealthShelterUserUserRegistrationSerializer


class HealthShelterPostView(APIView):
    def post(self, request):
        # check logged in user
        if request.user and request.user.is_authenticated and request.user.is_health_shelter:
            serializer = HealthShelterPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user.health_shelter_user)
                return Response(
                    {"status": "Post created successfully.", "data": serializer.data}
                )
            return Response(serializer.errors)
        return Response({"error": "User has to be logged in to create post."})

    def put(self, request, post_id=None):
        if post_id is None:
            return Response({"error": "Post ID is required"}, status=400)

        post = HealthShelterPost.objects.get(id=post_id)
        serializer = HealthShelterPostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "Post updated successfully.", "data": serializer.data}
            )
        return Response(serializer.errors)

    def get(self, request):
        if request.GET.get("all") == "true":
            posts = HealthShelterPost.objects.all().order_by("-created_on")
            serializer = HealthShelterPostSerializer(posts, many=True)
            return Response(serializer.data)

        if request.user and request.user.is_authenticated and request.user.is_health_shelter:
            posts = HealthShelterPost.objects.filter(
                user=request.user.health_shelter_user
            )
            serializer = HealthShelterPostSerializer(posts, many=True)
            return Response(serializer.data)

        return Response({"error": "User has to be logged in to view posts."})
