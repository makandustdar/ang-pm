from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .utils import send_review_order
import time

from review.models import Review


@shared_task(name='check_review_due')
def check_review_due(*args, **kwargs):
    for review in Review.objects.all():
        period_scale = review.reviewPeriod
        # if period_scale == 'seconds':
        #     if abs(int(time.time()) - int(review.last_sms)) >= review.reviewCount:
        #         send_review_order(review.machineName, '09300629575')
        #         review.last_sms = int(time.time())
        #         review.save()

        if period_scale == 'day':
            if abs(int(time.time()) - int(review.last_sms)) >= review.reviewCount * 86400:
                print('sent daily sms')
                send_review_order(review.machineName, '09300629575')
                review.last_sms = int(time.time())
                review.save()
        elif period_scale == 'month':
            if abs(int(time.time()) - int(review.last_sms)) >= review.reviewCount * 2629800:
                send_review_order(review.machineName, '09300629575')
                review.last_sms = int(time.time())
                review.save()
        elif period_scale == 'year':
            if abs(int(time.time()) - int(review.last_sms)) >= review.reviewCount * 31557600:
                send_review_order(review.machineName, '09300629575')
                review.last_sms = int(time.time())
                review.save()
