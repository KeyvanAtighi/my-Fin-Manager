from rest_framework import generics
from .models import Transaction
from accounts.models import Account
from .serializers import TransactionSerializer
from django.db import transaction as db_transaction
from .helpers import apply_transaction_effect, reverse_transaction_effect



class TransactionListCreateApiView(generics.ListCreateAPIView):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer
  
  @db_transaction.atomic
  def perform_create(self, serializer):
    instance = serializer.save()
    apply_transaction_effect(instance)

class TransactionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer

  @db_transaction.atomic
  def perform_update(self, serializer):
    old_instance = self.get_object()
    reverse_transaction_effect(old_instance)

    new_instance = serializer.save()
    apply_transaction_effect(new_instance)

  @db_transaction.atomic
  def perform_destroy(self, instance):
    reverse_transaction_effect(instance)
    instance.delete()

  
