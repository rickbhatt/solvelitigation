from django.contrib import admin

from .models import CustomUser

from django.contrib.auth.admin import UserAdmin 

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'phone_no')
    ordering= ('full_name',)
    search_fields= ('email', 'phone_no', 'date_joined')

    fieldsets = (
        (None, {'fields':('email','full_name','phone_no','age','state','regd_as','professional_opted_for','date_joined','last_login','password',),}),
        ('Permissions',{'fields': ('is_staff', 'is_active','is_superuser' ,'groups', 'user_permissions',)}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','full_name','phone_no','age','state','regd_as','professional_opted_for','date_joined','password1','password2',)}
         ),
    )

    

# class CustomUserAdmin(UserAdmin):
#     list_display = ('first_name', 'email',
#                     'is_staff')

#     fieldsets