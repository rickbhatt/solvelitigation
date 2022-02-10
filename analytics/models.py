from django.db import models

# Create your models here.


class VisitorCount(models.Model):

    ip = models.TextField(null=True)
    date_of_record = models.DateTimeField(null=True)