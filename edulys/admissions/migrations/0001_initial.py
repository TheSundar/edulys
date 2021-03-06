# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-07 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=1000)),
                ('address2', models.CharField(blank=True, max_length=1000, null=True)),
                ('city', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=1000)),
                ('pincode', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AllImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ClassFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('school_pricipal', models.CharField(max_length=1000)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.Address')),
                ('images', models.ManyToManyField(blank=True, null=True, to='admissions.AllImages')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.School')),
            ],
        ),
        migrations.CreateModel(
            name='Sylabuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.School')),
            ],
        ),
        migrations.AddField(
            model_name='classfee',
            name='from_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='From', to='admissions.SchoolClass'),
        ),
        migrations.AddField(
            model_name='classfee',
            name='sylabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admissions.Sylabuss'),
        ),
        migrations.AddField(
            model_name='classfee',
            name='to_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to', to='admissions.SchoolClass'),
        ),
    ]
