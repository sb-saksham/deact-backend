from django.db import models
from siwe_auth.models import AbstractWallet


ACCOUNT_TYPE_CHOICES = [
    ('ind', "Individual"),
    ('company', "Company/Organisation"),
    ('institution', "Educational Institution")
]


class UserModel(AbstractWallet):
    email = models.EmailField(max_length=264, unique=True)
    name = models.CharField(max_length=264, null=True, blank=True)
    account_type = models.CharField(choices=ACCOUNT_TYPE_CHOICES, default='ind', max_length=100)
