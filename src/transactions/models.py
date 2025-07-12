from django.db import models
from django.utils import timezone
from accounts.models import Account
# exception handling
from django.core.exceptions import ValidationError

def tz_aware_date():
    return timezone.localtime(timezone.now()).date()

class Transaction(models.Model):
  TRANSACTION_TYPE_CHOICES = [
    ('income', 'Income'),
    ('expense', 'Expense'),
    ('transfer', 'Transfer'),
  ]

  account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
  type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
  amount = models.IntegerField()
  date_occurred = models.DateField(default=tz_aware_date)
  description = models.CharField(max_length=255, blank=True, null=True)
  transfer_account = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='transfer_transactions', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.get_type_display()} of {self.amount} on {self.date_occurred} for {self.account.name}"
  
  # exception handling
  def clean(self):
    if self.amount <= 0:
        raise ValidationError('Amount must be positive.')
     
    if self.type == 'transfer':
      if not self.transfer_account:
          raise ValidationError('when transaction type is transfer, transfer account can not be null')
        
      if self.account == self.transfer_account:
          raise ValidationError('Can not transfer to the same account.')
    if self.type != 'transfer' and self.transfer_account:
        raise ValidationError('when type is not transfer, transfer account must be null')
     
  def save(self, *args, **kwargs):
     self.full_clean()
     super().save(*args, **kwargs)