

from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'messages', views.MessageViewSet, base_name='message')
router.register(r'conversations', views.ConversationViewSet, base_name='conversation')
router.register(r'profiles', views.ProfileViewSet, base_name='profile')
