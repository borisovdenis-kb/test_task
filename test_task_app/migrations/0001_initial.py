# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-06 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claims',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sent_date', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'permissions': (('view_claim', 'Can see one or several claims.'), ('send_claim', 'Can send claim.')),
            },
        ),
        migrations.CreateModel(
            name='CreditOrganizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('rotation_start_date', models.DateTimeField()),
                ('rotation_end_date', models.DateTimeField()),
                ('title', models.CharField(max_length=256)),
                ('offer_type', models.CharField(max_length=30)),
                ('scoring_min', models.IntegerField()),
                ('scoring_max', models.IntegerField()),
                ('credit_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_task_app.CreditOrganizations')),
            ],
        ),
        migrations.CreateModel(
            name='WorkSheets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('birth_day', models.DateField()),
                ('phone', models.CharField(max_length=12)),
                ('passport_number', models.CharField(max_length=10)),
                ('scoring', models.IntegerField()),
            ],
            options={
                'permissions': (('view_worksheet', 'Can see one or several worksheets.'),),
            },
        ),
        migrations.AddField(
            model_name='claims',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_task_app.Offers'),
        ),
        migrations.AddField(
            model_name='claims',
            name='worksheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_task_app.WorkSheets'),
        ),
    ]