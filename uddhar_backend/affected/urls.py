from django.urls import path
from .views import AffectedRequestView, AffectedUserView

urlpatterns = [
    path("profile/", AffectedUserView.as_view(), name="affected_user"),
    path("request/", AffectedRequestView.as_view(), name="affected_request"),
]
