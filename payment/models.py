
from django.db import models
from datetime import timezone

import razorpay

from account.models import CustomUser


SUB_CHOICES = (
('monthly', 'monthly'),
('quaterly', 'quaterly'),
('hf', 'half_yearly'),
('anually', 'anually'),
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
    tansaction_id = models.CharField(max_length=100, null = True)
    is_active = models.BooleanField(default= False)
    subscribed_on = models.DateTimeField(null=True)
    expiring_on = models.DateTimeField(null=True)

 



