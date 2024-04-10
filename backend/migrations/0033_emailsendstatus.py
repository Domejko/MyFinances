# Generated by Django 5.0.4 on 2024-04-06 19:46
from __future__ import annotations

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0032_client_email_verified"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailSendStatus",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("recipient", models.TextField()),
                ("aws_message_id", models.CharField(blank=True, editable=False, max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("send", "Send"),
                            ("reject", "Reject"),
                            ("bounce", "Bounce"),
                            ("complaint", "Complaint"),
                            ("delivery", "Delivery"),
                            ("open", "Open"),
                            ("click", "Click"),
                            ("rendering_failure", "Rendering_Failure"),
                            ("delivery_delay", "Delivery_Delay"),
                            ("subscription", "Subscription"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="emails_created", to="backend.team"
                    ),
                ),
                (
                    "sent_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="emails_sent",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="emails_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
