from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = "__all__"

    def validate_name(self, name):
      if not name.strip():
        raise serializers.ValidationError('Account name is required')
      return name
      
    def validate_balance(self, balance):
      if balance < 0:
        raise serializers.ValidationError('Account balance cannot be negative')
      return balance