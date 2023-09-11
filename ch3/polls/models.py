from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_positive(value):
    if value <= 0:
        raise ValidationError("0이하는 입력되지 않습니다.")


class mytable(models.Model):
    name = models.CharField(max_length=100, null=False)
    number = models.IntegerField(null=False)
    nickname = models.CharField(max_length=100, null=False)
    deposit = models.BigIntegerField(validators=[validate_positive], null=False)
    score = models.IntegerField()
