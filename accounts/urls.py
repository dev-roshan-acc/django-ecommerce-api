from django.urls import path
from .views import RegisterCustomerView,ListUserAdminView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path(
        "customer/register/",
        RegisterCustomerView.as_view(),
        name="customer-register",
    ),
    
     path(
        "users/",
        ListUserAdminView.as_view(),
        name="user-manage",
    ),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
