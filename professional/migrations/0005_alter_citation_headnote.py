# Generated by Django 3.2.8 on 2022-02-02 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0004_citation_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='headnote',
            field=models.TextField(help_text='required', null=True),
        ),
    ]
