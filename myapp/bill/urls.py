from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('bills', views.bills, name='about'),
    path('create', views.create, name='create'),
    path('bills/<int:pk>', views.BillsDetailView.as_view(), name='bill-details'),
    path('bills/<int:pk>/update', views.BillsUpdateView.as_view(), name='bill-update'),
    path('bills/<int:pk>/delete', views.BillsDeleteView.as_view(), name='bill-delete'),
    path('bills/filter<int:pk>', views.bills_filter, name='bills_filter'),
    path('bills/total', views.total_price, name='total-price'),
    path('sound', views.sound, name='sound'),
]
