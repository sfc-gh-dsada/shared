# Generated by Django 3.1.6 on 2021-07-29 21:15

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("core", "0004_pull_user_provided_base_sha")]

    operations = [
        migrations.CreateModel(
            name="ProfilingCommit",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("external_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("last_joined_uploads_at", models.DateTimeField(null=True)),
                ("last_summarized_at", models.DateTimeField(null=True)),
                ("joined_location", models.TextField(null=True)),
                ("summarized_location", models.TextField(null=True)),
                ("version_identifier", models.TextField()),
                (
                    "repository",
                    models.ForeignKey(
                        db_column="repoid",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profilings",
                        to="core.repository",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="ProfilingUpload",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("external_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("raw_upload_location", models.TextField()),
                (
                    "profiling_commit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="uploads",
                        to="profiling.profilingcommit",
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
