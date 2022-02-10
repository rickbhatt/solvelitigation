from django.contrib.auth.base_user import BaseUserManager

from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):

# CUSTOM USER MODEL WHERE THE EMAIL IS USED FOR AUTHORISATION 

    def create_superuser(self, email, full_name, password, **other_fields):
         
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)


        if other_fields.get('is_staff') is not True:
            raise ValueError(_('is staff must be set to true'))
        
        if other_fields.get('is_superuser') is not True:
            raise ValueError(_('is superuser must be set to true'))

        return self.create_user(email, full_name, password, **other_fields)

    def create_user(self, email, full_name, password, **other_fields):

        if not email:
            raise ValueError(_('The email must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name,**other_fields)
        user.set_password(password)
        user.save()
        return user