# Generated by Django 5.1.1 on 2024-10-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_control', '0010_rename_preparats_assignment_preparats_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_profile',
            name='adress',
            field=models.CharField(default='Адрес не указан', max_length=100),
        ),
        migrations.AddField(
            model_name='doctor_profile',
            name='self_description',
            field=models.TextField(default='Ничего не известно'),
        ),
        migrations.AlterField(
            model_name='pacient_profile',
            name='adress',
            field=models.CharField(default='Адрес не указан', max_length=100),
        ),
    ]