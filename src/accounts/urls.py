from django.urls import path
from .views import AccountListCreateApiView, AccountRetrieveUpdateDestroyApiView

urlpatterns = [
  path('/', AccountListCreateApiView.as_view(), name='account-list-create'),
  path('/<int:pk>/', AccountRetrieveUpdateDestroyApiView.as_view(), name='account-detail')
]