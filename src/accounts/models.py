from django.db import models
from django.core.exceptions import ValidationError

class Account(models.Model):

  name = models.CharField(max_length=100, unique=True, null=False)
  balance = models.IntegerField(default=0, editable=False)
  created_at = models.DateTimeField(auto_now_add=True)
  last_modify = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
  def clean(self):
    if self.balance < 0:
      raise ValidationError('Account balance can not be negative.')
    if not self.name.strip():
      raise ValidationError("Account name can not be empty")

  def save(self, *args, **kwargs):
    self.full_clean()
    super().save(*args, **kwargs)