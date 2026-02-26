from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class CustomTokenView(TokenObtainPairView):
    permission_classes = [AllowAny]

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenView.as_view(), name='login'),
]