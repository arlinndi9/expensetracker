import datetime

from django.db import models

# Create your models here.
class expensive(models.Model):

    description=models.CharField(max_length=255)
    amount=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.description}'
