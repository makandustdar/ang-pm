from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ReviewList.as_view(), name='review_list'),
    path('add/', views.review_add, name='review_add'),
    path('edit/<reviewId>/', views.review_edit, name='review_edit'),
    path('detail/<reviewId>/', views.review_detail, name='review_detail'),

    path('machine/list/', views.MachineList.as_view(), name='machine_list'),
    path('machine/add/', views.machine_add, name='machine_add'),
    path('machine/edit/<machineId>/', views.machine_edit, name='machine_edit'),

    path('part/list/', views.PartList.as_view(), name='part_list'),
    path('part/add/', views.part_add, name='part_add'),
    path('part/edit/<partId>/', views.part_edit, name='part_edit'),

    path('task/add/<reviewId>/', views.reviewtask_add, name='reviewtask_add'),
    path('task/edit/', views.reviewtask_edit, name='reviewtask_edit'),
]