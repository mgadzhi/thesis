from django.contrib import auth
from django.db import models

# Create your models here.


class User(auth.models.AbstractUser):

    ADMIN = 'AD'
    RESELLER = 'RS'
    AGENT = 'AG'

    USER_TYPES = (
        (ADMIN, 'admin'),
        (RESELLER, 'reseller'),
        (AGENT, 'agent'),
    )

    reseller = models.ForeignKey('self', db_index=True, null=True, default=None, related_name='agents')
    user_type = models.CharField(max_length=2, choices=USER_TYPES, default=AGENT)


    @property
    def is_admin(self):
        return self.user_type == self.ADMIN

    @property
    def is_reseller(self):
        return self.user_type == self.RESELLER

    @property
    def is_agent(self):
        return self.user_type == self.AGENT
