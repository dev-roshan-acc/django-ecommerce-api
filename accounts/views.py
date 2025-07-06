from django.shortcuts import render

from rest_framework import generics, permissions
from .serializers import CustomerRegisterSerializer, CreateNewUserAdminSerializer
from accounts.models.admin import Admin
from utils.permission_utils import HasPermission


# Create your views here.


class RegisterCustomerView(generics.CreateAPIView):
    serializer_class = CustomerRegisterSerializer
    permission_classes = [permissions.AllowAny]


class ListUserAdminView(generics.ListCreateAPIView):

    serializer_class = CreateNewUserAdminSerializer
    queryset = Admin.objects.all()

    # permission_classes = [permissions.IsAdminUser, HasPermission('manage_users')]
    # The line `permission_classes = [permissions.IsAdminUser, HasPermission('manage_users')]` in the
    # `ListUserAdminView` class is defining the permissions required to access the view.
    def get_permissions(self):
        return [permissions.IsAdminUser(), HasPermission("manage_users")]

    def perform_create(self, serializer):
        return serializer.save()
