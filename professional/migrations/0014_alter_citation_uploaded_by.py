# Generated by Django 3.2.8 on 2022-02-09 18:33

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professional', '0013_alter_citation_party_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='uploaded_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, on_update=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
