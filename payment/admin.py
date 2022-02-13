from django.contrib import admin

from . models import ServiceProduct,  UserSubscription

@admin.register(ServiceProduct)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'monthly_price','quaterly_price','hf_price')
    ordering= ('code',)
    search_fields= ('code',)


@admin.register(UserSubscription)
class  UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_choosen', 'is_active', 'subscribed_on',  'expiring_on')
    search_fields= ('user',)

