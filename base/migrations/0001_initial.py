# Generated by Django 3.2 on 2023-09-27 10:20

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='department_operations', to='base.department')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operationName', models.CharField(blank=True, max_length=300, null=True)),
                ('departmentName', models.CharField(blank=True, max_length=300, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('orderId', models.CharField(max_length=50)),
                ('publish', models.BooleanField(default=True)),
                ('is_for_machine', models.BooleanField(default=False)),
                ('is_for_department', models.BooleanField(default=False)),
                ('isConfirmed', models.BooleanField(default=False)),
                ('priority', models.CharField(blank=True, max_length=5, null=True)),
                ('status', models.CharField(choices=[('SV', 'ثبت شده'), ('SE', 'مشاهده شده'), ('DG', 'در حال انجام'), ('WG', 'در انتظار قطعه'), ('ST', 'ارسال به پیمانکار'), ('DN', 'تکمیل شده')], default='SV', max_length=2)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.department')),
                ('operation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='base.operation')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='base.operation')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('description2', ckeditor_uploader.fields.RichTextUploadingField()),
                ('date', models.DateField(null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('publish', models.BooleanField(default=True)),
                ('hours', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('SV', 'ثبت شده'), ('SE', 'مشاهده شده'), ('DG', 'در حال انجام'), ('WG', 'در انتظار قطعه'), ('ST', 'ارسال به پیمانکار'), ('DN', 'تکمیل شده')], default='SV', max_length=2, null=True)),
                ('operators', models.ManyToManyField(null=True, related_name='operator_tasks', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='base.order')),
                ('parts', models.ManyToManyField(related_name='task_parts', to='base.Part')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stuffs', to='base.department')),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pieces', to='base.order')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.part')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='part',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order', to='base.part'),
        ),
        migrations.AddField(
            model_name='order',
            name='stuff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_stuff', to='base.stuff'),
        ),
        migrations.AddField(
            model_name='order',
            name='subGroup',
            field=models.ManyToManyField(to='base.Subgroup'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='operation',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='station_operations', to='base.station'),
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together={('operation', 'description')},
        ),
    ]