from django.urls import path
from .views import HealthShelterRegistrationView, HealthShelterPostView

urlpatterns = [
    path(
        "register/",
        HealthShelterRegistrationView.as_view(),
        name="health_shelter_register",
    ),
    path(
        "health_shelter_post/",
        HealthShelterPostView.as_view(),
        name="health_shelter_post",
    ),
    path(
        "health_shelter_post/<int:post_id>",
        HealthShelterPostView.as_view(),
        name="health_shelter_post",
    ),
]
