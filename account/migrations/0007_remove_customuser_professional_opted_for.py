# Generated by Django 3.2.8 on 2022-02-13 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_customuser_subscribtion_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='professional_opted_for',
        ),
    ]
