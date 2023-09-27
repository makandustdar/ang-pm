from django.contrib import admin
from .models import Order, Department, Task, Subgroup, Operation, Part, Station, Piece, Stuff


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'operation', 'department', 'orderId')
    list_filter = ('user', 'department', 'createdAt')
    search_fields = ['id', 'orderId']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'order']
    list_filter = ['user', 'status']
    search_fields = ['description', 'description2']


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'machine']


admin.site.register(Subgroup)
admin.site.register(Operation)
admin.site.register(Station)
admin.site.register(Piece)
admin.site.register(Stuff)
