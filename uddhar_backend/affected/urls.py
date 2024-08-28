from django.urls import path
from .views import AffectedRequestView, AffectedUserView, getCount

urlpatterns = [
    path("profile/", AffectedUserView.as_view(), name="affected_user"),
    path("request/", AffectedRequestView.as_view(), name="affected_request"),
    path("get_counts/", getCount.as_view(), name="counts"),
]
