# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BundleElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elements', to='backends.Bundle')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('frontimage', models.ImageField(blank=True, null=True, upload_to=None)),
                ('backimage', models.ImageField(blank=True, null=True, upload_to=None)),
                ('content_image', models.ImageField(blank=True, null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('date_added', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderBundles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='backends.Bundle')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundles', to='backends.Order')),
            ],
        ),
        migrations.AddField(
            model_name='bundleelement',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundles', to='backends.Element'),
        ),
    ]
