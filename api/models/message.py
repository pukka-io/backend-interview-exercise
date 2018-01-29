from django.db import models
from django.utils import timezone

from .profile import Profile
from .conversation import Conversation



class Message(models.Model):
    """
        Message model definition
    """

    QUESTION = 'question'
    RESPONSE = 'response'
    COMMENT = 'comment'
    ACTION = 'action'

    TYPE_VERBS = {
        QUESTION: 'asked',
        RESPONSE: 'responded to',
        COMMENT: 'commented'
    }

    TYPE_CHOICES = (
        (QUESTION, 'Question'),
        (RESPONSE, 'Response'),
        (COMMENT, 'Comment'),
        (ACTION, 'Action'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=COMMENT)

    created_at = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True,
                               related_name='messages')

    text = models.TextField(max_length=1000)

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE,
                                     related_name='messages')

    class Meta:
        ordering = ['-created_at']

    def infos(self):
        if self.type == self.ACTION:
            return "{action} {time}".format(
                action=self.text,
                time=self.created_at.strftime('on %x at %X')
            )

        return "{author} {verb} {conversation_author} on '{subject}' {time}".format(
            author=self.author.full_name,
            verb=self.TYPE_VERBS[self.type],
            conversation_author=self.conversation.author.full_name,
            time=self.created_at.strftime('on %x at %X')
        )

    def __str__(self):
        if self.text:
            return self.text
        return str(self.id)
