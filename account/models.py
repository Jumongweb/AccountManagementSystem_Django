from django.db import models
from .utility import generate_account_number


# Create your models here.

class Account(models.Model):
    account_number = models.CharField(max_length=10, default=generate_account_number, unique=True, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    pin = models.CharField(max_length=4)
    balance = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    ACCOUNT_TYPE = [
        ('SAV', 'SAVING'),
        ('CUR', 'CURRENT'),
        ('DOM', 'DOMICILIARY'),
    ]
    account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE, default='SAV')


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('DEB', 'DEBIT'),
        ('CRE', 'CREDIT'),
        ('TRA', 'TRANSFER'),
    ]

    TRANSACTION_STATUS = [
        ('S', 'SUCCESSFUL'),
        ('F', 'FAILED'),
        ('P', 'PENDING'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=3,choices=TRANSACTION_TYPE,default='CRE')
    transaction_time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    transaction_status = models.CharField(max_length=1, choices=TRANSACTION_STATUS, default='S')

