# Generated by Django 5.1.1 on 2024-10-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_control', '0011_doctor_profile_adress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_profile',
            name='gender',
            field=models.CharField(choices=[('Mr', 'Мужчина'), ('Ms', 'Женщина')], default=1, max_length=2),
        ),
    ]
