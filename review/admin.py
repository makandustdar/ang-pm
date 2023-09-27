from django.contrib import admin
from .models import ReviewTask, Review


class ReviewAdmin(admin.ModelAdmin):
    # readonly_fields = ('last_sms',)
    pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewTask)
# Register your models here.
