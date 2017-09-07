# ---------------------------------------------------------------
# Для того, что бы тестировать django файлы
# Вставлять обязательно перед импортом моделей!!!
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_task.settings")
django.setup()
# ---------------------------------------------------------------

from django.contrib.auth.models import Permission, Group


class InitGroup:
    PERMISSIONS = [
        'add_user', 'change_user', 'delete_user',
        'add_session', 'change_session', 'delete_session',
    ]

    def __init__(self, gp_name, perms):
        self.gp_name = gp_name
        self.permissions = InitGroup.PERMISSIONS + perms

    def init_group_permissions(self):
        """Функция инициализирует группу списком пермишиннов."""
        group = Group.objects.get_or_create(name=self.gp_name)[0]
        permissions = Permission.objects.filter(codename__in=self.permissions)

        # устанавливаем группе необходимые разрешения
        group.permissions.clear()
        group.permissions.set(permissions)


if __name__ == '__main__':
    superusers_perms_needed = [
        'add_claims', 'change_claims', 'delete_claims', 'view_claim', 'send_claim',
        'add_creditorganizations', 'change_creditorganizations', 'delete_creditorganizations',
        'add_offers', 'change_offers', 'delete_offers', 'view_offers',
        'add_worksheets', 'change_worksheets', 'delete_worksheets', 'view_worksheet'
    ]
    partners_perms_needed = [
        'add_claims', 'send_claim',
        'add_worksheets', 'view_worksheet'
    ]
    creditorg_perms_needed = [
        'view_claim',
        'add_offers', 'change_offers', 'delete_offers', 'view_offers',
    ]

    superusers_group = InitGroup("superusers", superusers_perms_needed)
    superusers_group.init_group_permissions()

    partners_group = InitGroup("partners", partners_perms_needed)
    partners_group.init_group_permissions()

    creditorg_group = InitGroup("creditorg", creditorg_perms_needed)
    creditorg_group.init_group_permissions()
