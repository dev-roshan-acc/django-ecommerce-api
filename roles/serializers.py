from rest_framework import serializers
from roles.models.role import Role


class CreateRoleSerializer(serializers.ModelSerializer):
    role_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Role
        Fields = ["role_id",'admin_id']
        
    def create(self, validated_data):
        role  = Role.objects.create(**validated_data)
        role.save()
        return super().create(validated_data)
