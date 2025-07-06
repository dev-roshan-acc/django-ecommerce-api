from rest_framework import serializers
from accounts.models.customer import Customer
from accounts.models.user import User
from accounts.models.admin import Admin
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext_lazy as _
from roles.models.admin_role import AdminRole
from roles.models.role import Role


class UserFieldsMixin(serializers.Serializer):
    email = serializers.EmailField(
        write_only=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message=_("Email is already exists")
            )
        ],
    )
    password = serializers.CharField(
        write_only=True, min_length=8, validators=[validate_password]
    )
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)


class UserRegisterSerializer(UserFieldsMixin, serializers.ModelSerializer):
    is_staff = serializers.BooleanField(default=False)
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        is_staff = validated_data.pop("is_staff", False)
        is_active = validated_data.pop("is_active", True)

        user = User.objects.create(
            is_staff=is_staff, is_active=is_active, **validated_data
        )
        user.set_password(password)
        user.save()
        return user


class CreateNewUserAdminSerializer(UserFieldsMixin, serializers.ModelSerializer):
    role_id = serializers.IntegerField(write_only=True)  # Add this line

    profile_picture = serializers.ImageField(allow_null=True, required=False)
    date_joined = serializers.DateField(required=True)
    phone_number = serializers.CharField(required=True)
    job_title = serializers.CharField(required=True)
    department = serializers.CharField(required=True)

    class Meta:
        model = Admin
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "profile_picture",
            "phone_number",
            "job_title",
            "department",
            "date_joined",
            "role_id",
        ]

    def create(self, validated_data):
        role_id = validated_data.pop("role_id")
        user_data = {
            "email": validated_data.pop("email"),
            "password": validated_data.pop("password"),
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
            "is_staff": True,
        }
        with transaction.atomic():
            user_serializer = UserRegisterSerializer()
            user = user_serializer.create(user_data)
            # role_data = {"user": user.id, "role": validated_data.pop("role_id")}

            admin = Admin.objects.create(user=user, **validated_data)
            role = Role.objects.get(id=role_id)
            AdminRole.objects.create(admin=admin, role=role)

        return admin


class CustomerRegisterSerializer(UserFieldsMixin, serializers.ModelSerializer):

    profile_picture = serializers.ImageField(allow_null=True, required=False)
    date_of_birth = serializers.DateField(required=True)
    phone_number = serializers.CharField(required=True)
    address_line1 = serializers.CharField(required=True)

    class Meta:
        model = Customer
        fields = [
            "email",
            "password",
            "first_name",
            "last_name",
            "profile_picture",
            "date_of_birth",
            "phone_number",
            "address_line1",
        ]

    def create(self, validated_data):
        user_data = {
            "email": validated_data.pop("email"),
            "password": validated_data.pop("password"),
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
            "is_staff": False,
        }

        with transaction.atomic():
            user_serializer = UserRegisterSerializer()
            user = user_serializer.create(user_data)

            customer = Customer.objects.create(user=user, **validated_data)

        return customer
