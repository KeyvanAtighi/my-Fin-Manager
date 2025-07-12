from django.core.exceptions import ValidationError

def apply_transaction_effect(transaction):
  if transaction.type == 'income':
    transaction.account.balance += transaction.amount
  elif transaction.type == 'expense':
    if transaction.account.balance < transaction.amount:
      raise ValidationError('Insufficient funds for expense.')
    transaction.account.balance -= transaction.amount
  elif transaction.type == 'transfer':
    if transaction.account.balance < transaction.amount:
      raise ValidationError('Insufficient funds for expense.')
    transaction.account.balance -= transaction.amount
    transaction.transfer_account.balance += transaction.amount
    transaction.transfer_account.save()
  transaction.account.save()


def reverse_transaction_effect(transaction):
    if transaction.type == 'income':
      transaction.account.balance -= transaction.amount
    elif transaction.type == 'expense':
      transaction.account.balance += transaction.amount
    elif transaction.type == 'transfer':
      transaction.account.balance += transaction.amount
      transaction.transfer_account.balance -= transaction.amount
      transaction.transfer_account.save()
    transaction.account.save()