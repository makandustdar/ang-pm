from django.utils import timezone
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from base.managers import PublishedManager

User = get_user_model()


class Order(models.Model):
    StatusChoices = (
        ('SV', 'ثبت شده'),
        ('SE', 'مشاهده شده'),
        ("DG", 'در حال انجام'),
        ("WG", "در انتظار قطعه"),
        ('ST', "ارسال به پیمانکار"),
        ("DN", "تکمیل شده")
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    operation = models.ForeignKey('Operation', on_delete=models.SET_NULL, null=True, related_name='order')
    operationName = models.CharField(max_length=300, blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    departmentName = models.CharField(max_length=300, blank=True, null=True)
    subGroup = models.ManyToManyField('Subgroup')
    createdAt = models.DateTimeField(auto_now_add=True)
    description = RichTextField(blank=True, null=True)
    orderId = models.CharField(max_length=50)
    publish = models.BooleanField(default=True)
    is_for_machine = models.BooleanField(default=False)
    is_for_department = models.BooleanField(default=False)
    isConfirmed = models.BooleanField(default=False)  # Confirmed by manager
    priority = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=128, choices=StatusChoices, default='SV')  # Which step is right now
    part = models.ForeignKey('Part', on_delete=models.SET_NULL, null=True, related_name='order')
    stuff = models.ForeignKey('Stuff', on_delete=models.SET_NULL, null=True, related_name='order_stuff')

    # second_status = models.CharField(max_length=2, blank=True, null=True, choices=StatusChoices, default='SV')
    # isCompleted = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManager()

    # class Meta:
    #     unique_together = ("operation", "description")

    def __str__(self):
        return str(self.orderId)

    @property
    def get_priority(self):
        if self.priority == '1':
            return 'کم'
        elif self.priority == '2':
            return 'متوسط'
        elif self.priority == '3':
            return 'زیاد'


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Operation(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='department_operations')
    station = models.ForeignKey('Station', on_delete=models.SET_NULL, null=True, related_name='station_operations')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Subgroup(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    TaskChoices = (
        ('SV', 'ثبت شده'),
        ('SE', 'مشاهده شده'),
        ("DG", 'در حال انجام'),
        ("WG", "در انتظار قطعه"),
        ('ST', "ارسال به پیمانکار"),
        ("DN", "تکمیل شده")
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='task')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = RichTextUploadingField()
    description2 = RichTextUploadingField()
    date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    publish = models.BooleanField(default=True)
    hours = models.CharField(max_length=20, blank=True, null=True)
    # completed = models.BooleanField(default=False)
    parts = models.ManyToManyField('Part', related_name='task_parts')
    operators = models.ManyToManyField(User, null=True, related_name='operator_tasks')
    status = models.CharField(max_length=2, blank=True, null=True, choices=TaskChoices, default='SV')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return f'{self.order.orderId}'

    @property
    def get_time_diff(self):
        from datetime import datetime, date
        try:
            time_diff = datetime.combine(date.today(), self.end_time) - datetime.combine(date.today(), self.start_time)
            return time_diff.total_seconds()
        except TypeError as e:
            return 0


class Piece(models.Model):
    part = models.ForeignKey('Part', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='pieces')
    count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'piece for {self.part.name}| count: {self.count}'


class Part(models.Model):
    name = models.CharField(max_length=200)
    machine = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name='parts')

    def __str__(self):
        return self.name


class Stuff(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='stuffs')

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
