from rest_framework.views import APIView
from rest_framework.response import Response

# serializers
from affected.serializers import AffectedRequestSerializer

# models
from affected.models import AffectedRequest


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
                serializer.save(user=request.user.affected_user)
            serializer.save()
            return Response(
                {"status": "Request created successfully.", "data": serializer.data}
            )
        return Response(serializer.errors)

    def get(self, request, format=None, *args, **kwargs):
        if request.user and request.user.is_authenticated and request.user.is_affected:
            requests = AffectedRequest.objects.filter(user=request.user.affected_user)
            serializer = self.serializer_class(requests, many=True)
            return Response(serializer.data)
        return Response({"error": "User has to be logged in to view requests."})
