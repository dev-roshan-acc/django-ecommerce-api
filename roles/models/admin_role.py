from django.db import models
from accounts.models import Admin
from .role import Role

class AdminRole(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='admin_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='admins')

    class Meta:
        unique_together = ('admin', 'role')

    def __str__(self):
        return f"{self.admin.user.email} - {self.role.name}"