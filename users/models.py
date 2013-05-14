from django.contrib import auth
from django.db import models

# Create your models here.
from django.utils.translation import ugettext


class User(auth.models.AbstractUser):

    ADMIN = 'AD'
    RESELLER = 'RS'
    AGENT = 'AG'

    USER_TYPES = (
        (ADMIN, 'admin'),
        (RESELLER, 'reseller'),
        (AGENT, 'agent'),
    )

    TYPES_DESCRIPTION = {
        ADMIN: ugettext("Admin"),
        RESELLER: ugettext("Reseller"),
        AGENT: ugettext("Agent"),
    }

    agent_reseller = models.ForeignKey('self', db_index=True, null=True, default=None, related_name='agents')
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

    def get_type(self):
        return self.TYPES_DESCRIPTION[self.user_type]


class AdminManager(models.Manager):
    def get_query_set(self):
        return super(AdminManager, self).get_query_set().filter(user_type=User.ADMIN)


class ResellerManager(models.Manager):
    def get_query_set(self):
        return super(ResellerManager, self).get_query_set().filter(user_type=User.RESELLER)


class AgentManager(models.Manager):
    def get_query_set(self):
        return super(AgentManager, self).get_query_set().filter(user_type=User.AGENT)


class Admin(User):
    objects = AdminManager()


class Reseller(User):
    objects = ResellerManager()


class Agent(User):
    objects = AgentManager()
