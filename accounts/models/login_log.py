

from django.db import models
from accounts.models.user import User
from django.utils import timezone
class LoginLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.email} logged in at {self.login_time}"