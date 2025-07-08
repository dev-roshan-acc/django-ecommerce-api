from django.shortcuts import render

from rest_framework import generics, permissions
from .serializers import CustomerRegisterSerializer, CreateNewUserAdminSerializer
from accounts.models.admin import Admin
from utils.permission_utils import HasPermission
from utils.api_response_utils import (BaseListCreateView,BaseCreateAPIView)


# Create your views here.


class RegisterCustomerView(BaseCreateAPIView):
    serializer_class = CustomerRegisterSerializer
    permission_classes = [permissions.AllowAny]


class ListUserAdminView(BaseListCreateView):

    serializer_class = CreateNewUserAdminSerializer
    queryset = Admin.objects.all()

    # permission_classes = [permissions.IsAdminUser, HasPermission('manage_users')]
    # The line `permission_classes = [permissions.IsAdminUser, HasPermission('manage_users')]` in the
    # `ListUserAdminView` class is defining the permissions required to access the view.
    def get_permissions(self):
        return [permissions.IsAdminUser(), HasPermission("manage_users")]

    def perform_create(self, serializer):
        return serializer.save()
