from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from mondo.exceptions import MondoApiException
from .utils import MondoClientStaging, refresh_access_token


class Profile(models.Model):

    mondo_user_id = models.CharField(max_length=255)
    mondo_account_id = models.CharField(null=True, max_length=255)
    refresh_token = models.CharField(null=True, max_length=255)
    user = models.OneToOneField(User, null=True)

    def generate_access_token(self, request):
        try:
            access_token, refresh_token = refresh_access_token(settings.MONDO_CLIENT_ID,
                                                               settings.MONDO_CLIENT_SECRET,
                                                               self.refresh_token)
            self.refresh_token = refresh_token
            request.session['access_token'] = access_token
            return True
        except MondoApiException:
            return None

    def get_api_client(self, request):
        if 'access_token' not in request.session:
            self.generate_access_token(request)
        return MondoClientStaging(request.session.get('access_token'))

    def populate_account(self, request):
        client = self.get_api_client(request)
        accounts = client.list_accounts()
        self.mondo_account_id = accounts[0].id
        self.save()

    def balance(self, request):
        client = self.get_api_client(request)
        balance = client.get_balance(self.mondo_account_id)
        return str(balance.amount) if balance else None


# Creating a profile create the associated user
@receiver(models.signals.pre_save, sender=Profile)
def _profile_create_user(sender, instance, **kwargs):  # pylint: disable=unused-argument
    if instance.user is None:
        user = User.objects.create(username=instance.mondo_user_id)
        instance.user = user
