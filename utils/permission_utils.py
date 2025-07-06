from utils.auth_utils import admin_has_permission
from rest_framework.permissions import BasePermission
class HasPermission(BasePermission):
    def __init__(self,permission_codename):
        self.permission_codename = permission_codename
        
    def has_permission(self, request, view):
        admin = request.user.admin
        return admin_has_permission(admin,self.permission_codename)