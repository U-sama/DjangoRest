from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from . import views

urlpatterns = [
    path('', views.api_home), #localhost:8000/api/
    path('auth/', ObtainAuthToken.as_view()), #localhost:8000/api/auth
]
