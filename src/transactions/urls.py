from django.urls import path
from .views import TransactionListCreateApiView, TransactionRetrieveUpdateDestroyAPIView

urlpatterns = [
  path('/', TransactionListCreateApiView.as_view(), name='transaction_list_create'),
  path('/<int:pk>/', TransactionRetrieveUpdateDestroyAPIView.as_view(), name='transaction_detail')
]