from django.urls import path
from . import views

app_name = 'topic'

urlpatterns = [
    path('', views.sales, name='sales'),
    path('sales/', views.sales, name='sales'),  # 可選
    path('submit_product/', views.handle_sales_form, name='handle_sales_form'),
]
