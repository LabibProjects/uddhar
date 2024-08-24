from django.urls import path
from .views import RescuerRegistrationView, AffectedUserView

urlpatterns = [
    path("register/", RescuerRegistrationView.as_view(), name="rescuer_register"),
    path("affected_users/", AffectedUserView.as_view(), name="affected_users"),
    path("affected_users/<int:user_id>", AffectedUserView.as_view(), name="affected_users"),
]
