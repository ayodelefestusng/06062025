# Generated by Django 5.2.1 on 2025-06-03 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_insight_llm_sentiment_sessiondata_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread_id', models.TextField()),
                ('checkpoint_ns', models.TextField()),
                ('data', models.BinaryField()),
            ],
        ),
    ]
