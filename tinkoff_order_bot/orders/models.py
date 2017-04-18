from django.db import models

# Create your models here.
from model_utils import choices


class Order(models.Model):
    number = models.AutoField(primary_key=True)

    CONFIRMED = 'C'
    NON_CONFIRMED = 'NC'
    REJECTED = 'RJ'

    STATUS_CHOICES = (
        (CONFIRMED, 'Confirmed'),
        (NON_CONFIRMED, 'Non confirmed'),
        (REJECTED, 'Rejected'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=NON_CONFIRMED,
    )

    def __str__(self):
        return 'Order {id}:{status}'.format(id=self.number, status=self.status)

