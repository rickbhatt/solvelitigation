# Generated by Django 3.2.8 on 2022-02-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0012_auto_20220207_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='party_name',
            field=models.TextField(help_text='required', null=True),
        ),
    ]
