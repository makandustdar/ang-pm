from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/login.html'), name='logout'),
    
    path('list/', views.UsersList.as_view(), name='users_list'),
    path('add/', views.user_add, name='user_add'),
    path('edit/<str:username>/', views.user_edit, name='user_edit'),
    path('delete/<int:pk>/', views.user_delete, name='user_delete'),
    path('role/list/', views.role_list, name='roles_list'),
    path('role/add/', views.role_add, name='role_add'),
    path('role/edit/<int:role_id>/', views.role_edit, name='role_edit'),

    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
]