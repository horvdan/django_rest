from datetime import datetime
from django.db import models

class Spending(models.Model):
    date = models.DateTimeField(default=datetime.now)
    amount = models.PositiveIntegerField()
    currency = models.CharField(max_length=3) #TODO: extract currency into a separate model
    description = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.amount}{self.currency} | {self.description}'