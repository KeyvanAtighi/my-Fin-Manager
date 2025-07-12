from rest_framework import generics
from .serializers import AccountSerializer
from .models import Account

class AccountListCreateApiView(generics.ListCreateAPIView):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer

class AccountRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Account.objects.all()
  serializer_class = AccountSerializer