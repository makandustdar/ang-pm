from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('orders/list/', login_required(views.OrdersList.as_view()), name='orders_list'),
    path('orders/completed/list/', views.OrdersCompletedList.as_view(), name='orders_completed_list'),
    path('order/add/', views.order_add, name='order_add'),
    path('order/edit/<orderId>/', views.order_edit, name='order_edit'),
    path('order/detail/<orderId>/', views.order_detail, name='order_detail'),
    path('order/invoice/<orderId>/', views.order_invoice, name='order_invoice'),
    path('order/change_status/<int:pk>/', views.change_order_status, name='change_order_status'),
    path('tasks/list/', views.TasksList.as_view(), name='tasks_list'),
    path('task/add/', views.task_add, name='task_add'),
    path('task/edit/<taskId>/', views.task_edit, name='task_edit'),
    path('task/detail/<taskId>/', views.task_detail, name='task_detail'),
    path('task/invoice/<taskId>/', views.task_invoice, name='task_invoice'),

    path('department/list/', views.DepartmentList.as_view(), name='department_list'),
    path('department/add/', views.department_add, name='department_add'),
    path('department/edit/<departmentId>/', views.department_edit, name='department_edit'),

    path('operation/list/', views.OperationList.as_view(), name='operation_list'),
    path('operation/add/', views.operation_add, name='operation_add'),
    path('operation/edit/<operationId>/', views.operation_edit, name='operation_edit'),

    path('subgroup/list/', views.SubgroupList.as_view(), name='subgroup_list'),
    path('subgroup/add/', views.subgroup_add, name='subgroup_add'),
    path('subgroup/edit/<subgroupId>/', views.subgroup_edit, name='subgroup_edit'),

    path('ajax/', include('base.ajax_urls')),

    path('persons_report/', views.WorkReportView.as_view(), name='persons_report'),
    path('machines_report/', views.MachineReportView.as_view(), name='machines_report'),

    path("archive-task/<int:pk>/", views.change_task_publish_status, name='archive-task'),
    path("archive-part/<int:pk>/", views.change_part_publish_status, name='archive-part'),
    path("archive-stuff/<int:pk>/", views.change_stuff_publish_status, name='archive-stuff'),
    path("archive-station/<int:pk>/", views.change_station_publish_status, name='archive-station'),
    path("archive-order/<int:pk>/", views.change_order_publish_status, name='archive-order'),
    path("archive-operation/<int:pk>/", views.change_operation_publish_status, name='archive-operation'),

    path('parts/', views.PartsList.as_view(), name='machine_parts_list'),
    path('part/edit/<int:part_id>/', views.PartsList.as_view(), name='machine_part_edit'),
    path('part/add/', views.machine_part_add, name='machine_part_add'),

    # path('stuff/edit/<int:stuff_id>/', views.StuffEdit.as_view(), name='department_stuff_edit'),

    path('stuff/', views.StuffList.as_view(), name='stuff_list'),
    path('stuff/add/', views.machine_stuff_add, name='stuff_add'),

    path('stations/', views.StationList.as_view(), name='station_list'),
    path('station/edit/<int:pk>/', views.StationList.as_view(), name='station_edit'),
    path('station/add/', views.station_add, name='station_add'),

]
