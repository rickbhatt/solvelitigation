from django.contrib import admin

from . models import ServiceProduct,  UserSubscription

@admin.register(ServiceProduct)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'monthly_price','quaterly_price','hf_price')
    ordering= ('code',)
    search_fields= ('code',)


# @admin.register(Membership)
# class MembershipAdmin(admin.ModelAdmin):
#     list_display = ('membership_type', 'razorpay_plan_id',)
#     search_fields= ('razorpay_plan_id',)

@admin.register(UserSubscription)
class  UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_choosen', 'tansaction_id', 'is_active', 'subscribed_on',  'expiring_on')
    search_fields= ('user',)

# @admin.register(Subscription)
# class SubscriptionAdmin(admin.ModelAdmin):
#     list_display = ('user_membership', 'razorpay_subscription_id',)
#     search_fields= ('razorpay_subscription_id',)