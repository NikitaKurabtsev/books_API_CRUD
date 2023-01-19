from django.contrib.auth.models import User
from rest_framework import generics, permissions

from registration.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
