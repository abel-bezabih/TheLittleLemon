# restaurant/urls.py

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu_items_list'),
    path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_item_detail'),
    path('bookings/', views.BookingView.as_view(), name='booking_list'),
    path('bookings/<int:pk>/', views.SingleBookingView.as_view(), name='booking_detail'),

    # Authentication Endpoints
    path('auth/', include('djoser.urls')),  # User registration & login
    path('auth/', include('djoser.urls.authtoken')),  # Token generation
]
