from django.db import models
from django.contrib.auth.models import User
from .utils import MondoClientStaging


class Profile(models.Model):

    mondo_user_id = models.CharField(max_length=255)
    mondo_account_id = models.CharField(max_length=255)
    user = models.OneToOneField(User)

    def balance(self):
        client = MondoClientStaging(
            'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjaSI6Im9hdXRoY2xpZW50XzAwMDA5NFB2SU5ER3pUM2s2dHo4'
            'anAiLCJleHAiOjE0NjA5ODExOTksImlhdCI6MTQ2MDgwODM5OSwianRpIjoidG9rXzAwMDA5N0Z2dHBSRkN4Z3BXZ'
            'GtocHgiLCJ1aSI6InVzZXJfMDAwMDk3RnUwcnFLU3lvMzJLZUxidCIsInYiOiI0In0.e1FFcZFZbGGLSMwTYSCxYX'
            'B-EG4HSIlJbALCKdyUP9g')
        balance = client.get_balance(self.mondo_account_id)
        return str(balance.amount) if balance else None
