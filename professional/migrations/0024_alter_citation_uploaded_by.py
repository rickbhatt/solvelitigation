# Generated by Django 3.2.8 on 2022-02-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0023_alter_citation_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='uploaded_by',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
