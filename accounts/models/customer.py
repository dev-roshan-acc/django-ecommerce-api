from django.db import models
class Customer(models.Model):
    profile_picture = models.ImageField(
        upload_to="customer_profile/", blank=True, null=True
    )
    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    newsletter_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return f"Customer: {self.user.email}"

