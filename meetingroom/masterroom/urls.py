
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/',MasterRoom_API.as_view(),name='Rooms'),
    path('create/',Booking_API.as_view(),name='Create'),
    path('search/',BookingSearchAPI.as_view(),name='search'),
]
