from django.urls import path
from .views import AffectedRequestView

urlpatterns = [
    path("request/", AffectedRequestView.as_view(), name="affected_request"),
]
