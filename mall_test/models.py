import logging
import uuid

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

logger = logging.getLogger("portone")


def generate_uid():
    return uuid.uuid4().hex


class Payment(models.Model):
    class StatusChoices(models.TextChoices):
        READY = "ready", "미결제"
        PAID = "paid", "결제완료"
        CANCELLED = "cancelled", "결제취소"
        FAILED = "failed", "결제실패"

    uid = models.UUIDField(default=generate_uid(), editable=False)
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="1원 이상의 금액을 지정해주세요."),
        ]
    )
    status = models.CharField(
        max_length=9,
        default=StatusChoices.READY,
        choices=StatusChoices.choices,
        db_index=True,
    )
    is_paid_ok = models.BooleanField(default=False, db_index=True)

    @property
    def merchant_uid(self) -> str:
        return str(self.uid)
