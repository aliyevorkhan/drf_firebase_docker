from django.conf import settings
from django.core.management.base import BaseCommand
from firebase_auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            email = settings.ADMIN_EMAIL
            password = settings.ADMIN_PASSWORD
            print('Creating User for %s (%s)' % (email, email))
            admin = User.objects.create_superuser(email=email, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
