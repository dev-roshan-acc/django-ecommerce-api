from django.db import models
from accounts.models.user import User
class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.CharField(max_length=100, blank=True)  # e.g. Sales, Support, IT
    job_title = models.CharField(max_length=100, blank=True)  # e.g. Manager, Supervisor
    phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(
        upload_to="admin_profiles/", blank=True, null=True
    )
    date_joined = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(
        default=True
    )  # To deactivate admin accounts without deleting

    # Optionally, you can add fields like last_login tracked separately, etc.

    def __str__(self):
        return f"Admin: {self.user.email}"

