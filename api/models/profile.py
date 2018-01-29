"""
    Define the Profile model
    This model represent a person and is the central
    'social' system to link people to actions in the app
"""

from django.db import models
from django.utils import timezone


class Profile(models.Model):

    email = models.EmailField()

    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)

    # account = models.ForeignKey('Account', on_delete=models.CASCADE,
    #                             related_name="profiles")
    job_title = models.CharField(max_length=200, blank=True, default='')

    points = models.IntegerField(default=0)

    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=timezone.now)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return '{full_name} - {job_title}'.format(
            full_name=self.full_name,
            job_title=self.job_title,
        )
