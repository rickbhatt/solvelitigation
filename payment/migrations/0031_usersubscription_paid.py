# Generated by Django 3.2.8 on 2022-02-13 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0030_usersubscription_subscription_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
