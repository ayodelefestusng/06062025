# Generated by Django 5.2.1 on 2025-06-04 19:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_insight_updated_at_insight_user_ticket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='session_id',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='insight',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
