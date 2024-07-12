from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(email="admin@exemple.com")
        user.set_password("pass")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

