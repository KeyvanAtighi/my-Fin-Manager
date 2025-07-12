from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Transaction
    fields = "__all__"

    def validate_amount(self, amount):
      if amount <= 0:
        raise serializers.ValidationError('Amount must be positive.')
      return amount
    
    def validate(self, data):
      transaction_type = data['type']
      transaction_account = data['account']
      transfer_account = data['transfer_account']

      if transaction_type == 'transfer':
        if not transfer_account:
          raise serializers.ValidationError('when type is transfer, transfer account can not be null')
        
        if transaction_account == transfer_account:
          raise serializers.ValidationError('Can not transfer to the same account.')
      if transaction_type != 'transfer' and transfer_account:
        raise serializers.ValidationError('when type is not transfer, transfer account must be null')
      return data