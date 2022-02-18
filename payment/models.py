
from django.db import models
from datetime import timezone

import razorpay

from account.models import CustomUser


SUB_CHOICES = (
('1', 'For 1 Month'),
('3', 'For 3 Months'),
('6', 'For 6 Months'),
('12', 'For 1 Year'),
)

PAYMENT_STATUS  = (
    ('1','success'),
    ('0', 'failure'),
)

class ServiceProduct(models.Model):
    
    title = models.CharField(max_length=50, null = True)
    code = models.IntegerField(null=True, unique= True)
    monthly_price = models.IntegerField(null=True)
    quaterly_price = models.IntegerField(null=True)
    hf_price = models.IntegerField(null=True)



    def __str__(self):
        return self.title  



class UserSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service_choosen = models.ForeignKey(ServiceProduct, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=True)
    subscription_duration = models.CharField(max_length=10, choices=SUB_CHOICES, null=True)
    subscribed_on = models.DateTimeField(null=True)
    expiring_on = models.DateTimeField(null=True)
    payment_id = models.CharField(max_length=100, null=True, unique=True)
    razorpay_order_id = models.CharField(max_length=100, null = True)
    razorpay_payment_id = models.CharField(max_length=100, null = True)
    razorpay_signature = models.CharField(max_length=100, null = True)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS, null=True)
    is_active = models.BooleanField(default= False)
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.payment_id is None and self.subscribed_on:
            self.payment_id = self.subscribed_on.strftime('SL%Y%m%d%M%SODR') + str(self.user.id) # SL- Solve Litigation, year, month, day, minute seconds, 'ODR', user id
        return super(UserSubscription, self).save(*args, **kwargs)

    def __str__(self):
        return self.get_subscription_duration_display()




 



