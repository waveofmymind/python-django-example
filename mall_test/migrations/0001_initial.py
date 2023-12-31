# Generated by Django 4.1.7 on 2023-12-28 01:58

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uid", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "amount",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                1, message="1원 이상의 금액을 지정해주세요."
                            )
                        ]
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ready", "미결제"),
                            ("paid", "결제 완료"),
                            ("cancelled", "결제 취소"),
                            ("failed", "결제 실패"),
                        ],
                        db_index=True,
                        default="ready",
                        max_length=9,
                    ),
                ),
                ("is_paid_ok", models.BooleanField(db_index=True, default=True)),
            ],
        ),
    ]
