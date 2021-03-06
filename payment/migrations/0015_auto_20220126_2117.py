# Generated by Django 3.2.8 on 2022-01-26 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_auto_20220126_1717'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='ServiceProduct',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='razorpay_customer_id',
        ),
        migrations.AddField(
            model_name='usermembership',
            name='service_choosen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.serviceproduct'),
        ),
        migrations.DeleteModel(
            name='Plan',
        ),
    ]
