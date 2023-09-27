from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from .models import *

import json


def confirm_order(request):
    data = json.loads(request.body)
    orderId = data['orderId']

    q = Order.objects.filter(orderId=orderId)
    # TODO change status on line 14 later
    if q.exists():
        q.update(isConfirmed=True, status=f'ارسال به واحد {q[0].departmentName}')
        message = {'status': 200, 'text': ''}
    else:
        message = {'status': 400, 'text': 'شماره سفارش صحیح نمیباشد'}

    return JsonResponse(message, safe=False)


def update_status(request):
    data = json.loads(request.body)
    id = data['id']
    db = data['db']
    status = data['value']

    if db == 'user':
        q = User.objects.filter(id=id)
        if status:
            q.update(is_active=True)
            message = {'status': '200', 'detail': f'{q[0].profile} فعال شد'}
        else:
            q.update(is_active=False)
            message = {'status': '200', 'detail': f'{q[0].profile} غیرفعال شد'}

    return JsonResponse(message, safe=False)


def get_parts(request):
    operation_id = request.GET.get('operation_id')
    operation = Operation.objects.get(id=operation_id)
    parts = list(operation.parts.values_list('name', 'pk'))
    message = {'data': parts}
    return JsonResponse(message, safe=False)


def get_stuff(request):
    department_id = request.GET.get('department_id')
    department = Department.objects.get(id=department_id)
    stuff = list(department.stuffs.values_list('name', 'pk'))
    message = {'data': stuff}
    return JsonResponse(message, safe=False)
