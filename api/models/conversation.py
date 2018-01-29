from django.db import models
from django.utils import timezone

from .profile import Profile


class Conversation(models.Model):
    """
        Conversation model definition
    """

    created_at = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE,
                               related_name='conversations')

    subject = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        if self.subject:
            return self.subject
        return str(self.id)
