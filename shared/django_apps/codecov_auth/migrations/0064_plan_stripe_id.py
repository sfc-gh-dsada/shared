# Generated by Django 4.2.16 on 2025-01-16 22:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("codecov_auth", "0063_tier_plan"),
    ]

    operations = [
        migrations.AddField(
            model_name="plan",
            name="stripe_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
