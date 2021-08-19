from datetime import datetime
from django.db import models
from api.validators import currency_code_validator

class Currency(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=3, validators=[currency_code_validator])
    
    def __str__(self):
        return self.code

class Spending(models.Model):
    date = models.DateTimeField(default=datetime.now)
    amount = models.PositiveIntegerField()
    description = models.CharField(max_length=30)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.amount}{self.currency} | {self.description}'

