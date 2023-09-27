from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import authenticate, login, update_session_auth_hash, get_user_model
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import *
from .forms import PasswordChangeForm

User = get_user_model()


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'نام کاربری یا رمز عبور صحیح نمیباشد')
        else:
            messages.error(request, 'خطایی رخ داده است')
    return render(request, 'auth/login.html')


class UsersList(ListView):
    model = User
    template_name = 'users/list.html'
    paginate_by = 10
    context_object_name = 'users'

    def get_queryset(self):
        users = User.objects.filter(is_superuser=False).order_by('-date_joined')

        q = self.request.GET.get('q')
        role = self.request.GET.get('role')
        status = self.request.GET.get('status')

        if q:
            users = users.filter(Q(username__contains=q) | Q(first_name__contains=q) | Q(last_name__contains=q))

        if role:
            users = users.filter(groups__id=role)

        if status:
            users = users.filter(is_active=status)

        return users

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roles'] = Group.objects.all()
        return context


def user_add(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        role = request.POST.get('role')
        department = request.POST.get('department')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'نام کابری ثبت شده است')
        else:

            user = User.objects.create_user(first_name=fname, last_name=last_name, username=username, email=email,
                                            password=password)
            # user.set_password(password)
            user.groups.add(Group.objects.get(id=role))
            print('before save')
            user.save()
            print('after save')
            # repair_operator_role = Group.objects.get(name='اپراتور فنی')
            # if int(role) == repair_operator_role.id:
            #     RepairOperator.objects.create(operator=user)

            profile = Profile.objects.get(user=user)
            profile.mobileNumber = mobile
            profile.department = Department.objects.get(id=department)
            profile.save()
            messages.success(request, 'کاربر ایجاد شد')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    departments = Department.objects.all()
    roles = Group.objects.all()
    context = {'roles': roles, 'departments': departments}
    return render(request, 'users/add.html', context)


def user_edit(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        role = request.POST.get('role')
        department = request.POST.get('department')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exclude(id=user.id).exists():
            messages.error(request, 'نام کابری ثبت شده است')
        else:
            user.first_name = fname.strip()
            user.last_name = last_name.strip()
            user.username = username
            user.email = email
            user.groups.clear()
            user.groups.add(Group.objects.get(id=role))
            if password:
                user.set_password(password)
            user.save()

            profile = Profile.objects.get(user=user)
            profile.department = Department.objects.get(id=department)
            profile.mobileNumber = mobile
            profile.save()
            messages.success(request, 'کاربر ویرایش شد')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    departments = Department.objects.all()
    roles = Group.objects.all()
    context = {'roles': roles, 'departments': departments, 'user': user}
    return render(request, 'users/edit.html', context)


def user_delete(request, pk):
    if request.method == 'POST':
        print(pk)
        User.objects.get(id=pk).delete()
        messages.success(request, 'کاربر با موفقیت حذف شد!')
        return redirect('users_list')


def role_list(request):
    roles = Group.objects.all()
    context = {'roles': roles}
    return render(request, 'roles/list.html', context)


def role_add(request):
    if request.method == 'POST':
        role_name = request.POST.get('roleName')
        permissions_list = request.POST.getlist('permission')

        if Group.objects.filter(name=role_name).exists():
            messages.error(request, 'نقش ایجاد شده است')
            return redirect('roles_list')
        elif permissions_list:
            role = Group.objects.create(name=role_name)

            for per in permissions_list:
                q = Permission.objects.filter(codename=per)
                if q.exists():
                    role.permissions.add(q[0])
                else:
                    if 'order' in per:
                        q = Permission.objects.create(codename=per, name='Can view order all', content_type_id=13)
                    elif 'task' in per:
                        q = Permission.objects.create(codename=per, name='Can view task all', content_type_id=13)
                    role.permissions.add(q)

            messages.success(request, 'نقش ایجاد شد')
            return redirect('roles_list')

    return render(request, 'roles/list.html')


def role_edit(request, role_id):
    role = Group.objects.get(id=role_id)
    if request.method == 'POST':
        role_name = request.POST.get('roleName')
        permissions_list = request.POST.getlist('permission')
        if Group.objects.filter(name=role_name).exclude(id=role_id).exists():
            messages.error(request, 'نقش ایجاد شده است')
            return redirect('roles_list')
        else:
            role.name = role_name
            role.save()

        if permissions_list:
            role.permissions.clear()
            for per in permissions_list:
                q = Permission.objects.filter(codename=per)
                if q.exists():
                    role.permissions.add(q[0])
                else:
                    if 'order' in per:
                        q = Permission.objects.create(codename=per, name='Can view order all', content_type_id=13)
                    elif 'task' in per:
                        q = Permission.objects.create(codename=per, name='Can view task all', content_type_id=13)
                    role.permissions.add(q)

            messages.success(request, 'نقش ویرایش شد')
            return redirect('roles_list')

    return render(request, 'roles/list.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'رمز عبور باموفقیت تغییر کرد')
            return redirect('logout')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {
        'form': form
    })


def profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exclude(id=request.user.id).exists():
            messages.error(request, 'نام کابری ثبت شده است')
        else:
            user.first_name = fname
            user.last_name = lname
            user.username = username
            user.email = email
            user.save()

            profile = Profile.objects.get(user=user)
            profile.mobileNumber = mobile
            profile.save()
            messages.success(request, 'پروفایل ویرایش شد')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    context = {'user': user}
    return render(request, 'users/profile.html', context)
