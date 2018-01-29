
from rest_framework import serializers

from .models import Message, Conversation, Profile

from .utils import instantiate_reward_message

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'last_name', 'full_name',
                  'job_title', 'points', 'is_admin', 'created_at')

        extra_kwargs = {
            'created_at': {'read_only': True},
            'points': {'read_only': True},
            'is_admin': {'read_only': True},
        }

class MessageSerializer(serializers.ModelSerializer):
    """
        Define how a message is serialized
    """

    author = ProfileSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(),
                                                   source='author',
                                                   write_only=True)

    class Meta:
        model = Message
        fields = ('id', 'type', 'author', 'author_id', 'conversation', 'text',
                  'infos', 'created_at')

        extra_kwargs = {
            'created_at': {'read_only': True},
            'type': {'read_only': True},
            'conversation': {'write_only': True},
        }

    def create(self, validated_data):
        message = Message.objects.create(**validated_data)
        message.author.points += 1
        message.author.save()
        return message


class ConversationSerializer(serializers.ModelSerializer):

    author = ProfileSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(),
                                                   source='author',
                                                   write_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ('id', 'subject', 'author', 'author_id', 'created_at', 'messages')

        extra_kwargs = {
            'created_at': {'read_only': True}
        }

class ConversationListSerializer(ConversationSerializer):
    class Meta(ConversationSerializer.Meta):
        fields = ('id', 'subject', 'author', 'author_id', 'created_at')
