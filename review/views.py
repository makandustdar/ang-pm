from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages

from .models import *
from .forms import *

import json


class ReviewList(ListView):
    model = Review
    template_name = 'review/list.html'
    context_object_name = 'reviews'
    paginate_by = 10

    def get_queryset(self):
        reviews = Review.objects.all().order_by('-createdAt')

        q = self.request.GET.get('q')
        machine = self.request.GET.get('department')
        part = self.request.GET.get('operation')

        if q:
            reviews = reviews.filter(
                Q(user__username__contains=q) | Q(user__first_name__contains=q) | Q(user__last_name__contains=q))

        if machine:
            reviews = reviews.filter(machine_id=machine)

        if part:
            reviews = reviews.filter(part_id=part)

        return reviews

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['machines'] = Machine.objects.all()
        context['parts'] = Part.objects.all()
        return context


def review_add(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            part = form.cleaned_data['part']
            machine = form.cleaned_data['machine']
            instance = form.save(commit=False)
            instance.user = request.user
            instance.partName = part.name
            instance.machineName = machine.name
            instance.save()

            messages.success(request, 'درخواست بازدید ثبت شد')
            return redirect('review_list')
    else:
        form = ReviewForm()

    context = {'form': form}
    return render(request, 'review/add.html', context)


def review_edit(request, reviewId):
    review = Review.objects.get(id=reviewId)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            part = form.cleaned_data['part']
            machine = form.cleaned_data['machine']
            instance = form.save(commit=False)
            instance.partName = part.name
            instance.machineName = machine.name
            instance.save()

            messages.success(request, 'درخواست بازدید ویرایش شد')
            return redirect('review_list')
    else:
        form = ReviewForm(request.POST or None, instance=review)

    context = {'form': form, 'review': review}
    return render(request, 'review/edit.html', context)


def review_detail(request, reviewId):
    review = Review.objects.get(id=reviewId)

    context = {'review': review}
    return render(request, 'review/detail.html', context)


class MachineList(ListView):
    model = Machine
    template_name = 'machine/list.html'
    paginate_by = 100
    context_object_name = 'machines'


def machine_add(request):
    if request.method == 'POST':
        name = request.POST.get('machineName')
        Machine.objects.get_or_create(name=name)
        messages.success(request, 'واحد ایجاد شد')
        return redirect('machine_list')


def machine_edit(request, machineId):
    if request.method == 'POST':
        name = request.POST.get('machineName')
        Machine.objects.filter(id=machineId).update(name=name)
        messages.success(request, 'واحد ویرایش شد')
        return redirect('machine_list')


class PartList(ListView):
    model = Part
    template_name = 'part/list.html'
    paginate_by = 100
    context_object_name = 'parts'


def part_add(request):
    if request.method == 'POST':
        name = request.POST.get('partName')
        description = request.POST.get('partDesc')
        part, created = Part.objects.get_or_create(name=name)
        part.description = description
        part.save()
        messages.success(request, 'قطعه ایجاد شد')
        return redirect('part_list')


def part_edit(request, partId):
    if request.method == 'POST':
        name = request.POST.get('partName')
        description = request.POST.get('partDesc')
        Part.objects.filter(id=partId).update(name=name, description=description)
        messages.success(request, 'قطعه ویرایش شد')
        return redirect('part_list')


def reviewtask_add(request, reviewId):
    review = Review.objects.get(id=reviewId)
    if request.method == 'POST':
        description = request.POST.get('description')
        done = request.POST.get('done')

        ReviewTask.objects.create(review=review, description=description, done=done)
        messages.success(request, 'بازدید ثبت شد')
        return redirect('review_list')


def reviewtask_edit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        description = data['description']
        done = data['done']
        taskId = data['taskId']

        print('taskId', taskId)

        ReviewTask.objects.filter(id=taskId).update(description=description, done=done)
        messages = {'status': 200, 'text': 'بازدید ویرایش شد'}
        return JsonResponse(messages, safe=False)
