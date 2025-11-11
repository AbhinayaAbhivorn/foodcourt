from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.user_items, name='user_items'),
    path('order-now/', views.order_now, name='order_now'),
    path('order-list/', views.order_list, name='order_list'),
]
