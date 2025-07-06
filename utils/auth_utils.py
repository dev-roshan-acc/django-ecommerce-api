from roles.models import Role, Permission


def admin_has_permission(admin, permission_codename):
    # roles = Role.objects.filter(admin_roles__admin=admin)
    return Permission.objects.filter(
        permission_roles__role__admin_roles__admin=admin, codename=permission_codename
    ).exists()
