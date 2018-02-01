
from rest_framework import status, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound


from api.serializers import (
    MessageSerializer,
    ConversationSerializer,
    ConversationListSerializer,
    ProfileSerializer,
)

from api.models import (
    Message,
    Conversation,
    Profile,
)


class MessageViewSet(GenericViewSet):
    """
        Api Message viewset
    """
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    def list(self, request):
        """
            Api enpoint that list all messages
        """
        messages = self.get_queryset()
        serializer = self.serializer_class(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
            Api endpoint that create a Message.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConversationViewSet(GenericViewSet):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()

    def list(self, request):
        conversations = self.get_queryset()
        serializer = ConversationListSerializer(conversations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        try:
            conversation = self.get_queryset().get(pk=pk)
        except Conversation.DoesNotExist:
            raise NotFound

        serializer = self.serializer_class(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        Conversation.objects.create(author_id=request.POST.get('author_id'), subject=request.POST.get('subject'))

        # TODO: Logic is missing
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
