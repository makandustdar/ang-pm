from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from base.models import Order, Subgroup, Piece, Task, Part, User

import pandas as pd

def user_login(request):
    import json

    # Opening JSON file
    f = open('order.json', encoding='utf8')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    for item in data:
        order_model, is_create = Order.objects.get_or_create(
            operation_id=item['fields']['operation'],
            operationName=item['fields']['operationName'],
            department_id=item['fields']['department'],
            departmentName=item['fields']['departmentName'],
            description=item['fields']['description'],
            orderId=item['fields']['orderId'],
            publish=item['fields']['publish'],
            is_for_machine=item['fields']['is_for_machine'],
            is_for_department=item['fields']['is_for_department'],
            isConfirmed=item['fields']['isConfirmed'],
            priority=item['fields']['priority'],
            status=item['fields']['status'],
            part_id=item['fields']['part'],
            stuff_id=item['fields']['stuff'],
            user_id=User.objects.get(username=item['fields']['user'][0]).id,
        )
        print(order_model)
        if is_create and item['fields']['subGroup']:
            order_model.subGroup.add(Subgroup.objects.get(id=item['fields']['subGroup'][0]))
            order_model.save()

        df = pd.read_json('Piece.json')
        result = df[df['fields'].apply(lambda x: x.get('order', 0) == 525)]
        for index, row in result.iterrows():
            fields = row['fields']
            Piece.objects.create(
                order_id=order_model.id,
                part_id=fields['part'],
                count=fields['count']
            )

        df = pd.read_json('task.json')
        result = df[df['fields'].apply(lambda x: x.get('order', 0) == 525)]
        for index, row in result.iterrows():
            fields = row['fields']
            task = Task.objects.create(
                order_id=order_model.id,
                user_id=fields['user'][0],
                description=fields['description'],
                description2=fields['description2'],
                publish=fields['publish'],
                hours=fields['hours'],
                status=fields['status'],
            )
            if fields['parts']:
                task.parts.add(Part.objects.get(id=fields['parts'][0]))
            if fields['operators']:
                for o in fields['operators']:
                    task.operators.add(User.objects.get(username=o[0]))
            task.save()




urlpatterns = [
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('adminbia2/', admin.site.urls),
                  path('', include('base.urls')),
                  path("import/", user_login),
                  path('users/', include('users.urls')),
                  path('review/', include('review.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
