from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .api_views import CharacterViewSet

router = DefaultRouter()
router.register('characters', CharacterViewSet, basename='character-api')

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='api_token'),
    path('', include(router.urls)),
]
