# Generated by Django 3.2.8 on 2022-01-31 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citation',
            old_name='date',
            new_name='date_of_order',
        ),
    ]
