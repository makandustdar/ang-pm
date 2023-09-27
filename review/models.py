import datetime
import time
from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    part = models.ForeignKey('Part', on_delete=models.SET_NULL, null=True)
    partName = models.CharField(max_length=300)
    machine = models.ForeignKey('Machine', on_delete=models.SET_NULL, null=True)
    machineName = models.CharField(max_length=300)
    reviewPeriod = models.CharField(max_length=200)
    last_sms = models.CharField(default=time.time(), max_length=100)
    # last_sms.editable = True
    reviewCount = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'بازدید {self.partName} {self.machineName}'

    @property
    def get_reviewPeriod(self):
        if self.reviewPeriod == 'day':
            return 'روز'
        elif self.reviewPeriod == 'month':
            return 'ماه'
        elif self.reviewPeriod == 'year':
            return 'سال'


class Part(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class Machine(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class ReviewTask(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
