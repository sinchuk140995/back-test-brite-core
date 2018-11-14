# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 23:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('risks', '0004_auto_20181112_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=255, verbose_name='value')),
            ],
        ),
        migrations.CreateModel(
            name='ClientInsuranceRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post date')),
                ('insurance_risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_risks', to='risks.InsuranceRisk', verbose_name='insurance risk')),
            ],
            options={
                'ordering': ('-post_date',),
            },
        ),
        migrations.AddField(
            model_name='clientfield',
            name='client_insurance_rik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_fields', to='clients.ClientInsuranceRisk', verbose_name='client insurance risk'),
        ),
        migrations.AddField(
            model_name='clientfield',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_fields', to='risks.Field', verbose_name='field'),
        ),
        migrations.AddField(
            model_name='clientfield',
            name='select_option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_options', to='risks.SelectOption', verbose_name='selected option'),
        ),
    ]