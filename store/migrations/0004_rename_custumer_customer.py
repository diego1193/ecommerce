# Generated by Django 4.2.11 on 2024-04-30 04:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Custumer',
            new_name='Customer',
        ),
    ]
