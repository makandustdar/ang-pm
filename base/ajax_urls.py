from django.urls import path
from . import ajax_views as views

urlpatterns = [
    path('confirm-order/', views.confirm_order),
    path('update-status/', views.update_status),
    path('get-parts/', views.get_parts),
    path('get-stuff/', views.get_stuff)
]
