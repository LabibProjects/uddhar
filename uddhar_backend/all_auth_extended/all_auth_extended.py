from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        return f"{emailconfirmation.key}"


# Social Login
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from affected.models import AffectedUser


@receiver(user_signed_up)
def create_consumer_profile(request, user, **kwargs):
    # Check if the user signed up through social authentication
    sociallogin = kwargs.get("sociallogin")
    if sociallogin and sociallogin.account.provider == "google":
        # Extract the first_name from user data
        name = sociallogin.account.extra_data.get("name", "")
        print(name)
        # Create an AffectedUser object
        AffectedUser.objects.create(user=user, name=name)
        user.is_affected = True
        user.save()
