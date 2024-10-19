# Generated by Django 5.1.1 on 2024-10-14 06:34

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight_control', '0002_pacient_profile_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diets_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('foto_file_path', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Diseases_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('diseases_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Preparats_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('foto_file_path', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='pacient_profile',
            name='email',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='pacient_profile',
            name='registration_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.CreateModel(
            name='Accompanying_disease_pacients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_list_id', models.ManyToManyField(to='weight_control.diseases_list')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('doc_stage', models.IntegerField(max_length=2)),
                ('registration_date', models.DateField(blank=True, default=datetime.date.today)),
                ('foto_file_path', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('doc_specialty', models.ManyToManyField(to='weight_control.specialty_list')),
            ],
        ),
        migrations.CreateModel(
            name='Doc_ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('patient_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='weight_control.pacient_profile')),
                ('doctor_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='weight_control.doctor_profile')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assign_date', models.DateField(blank=True, default=datetime.date.today)),
                ('description', models.TextField()),
                ('user_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='weight_control.pacient_profile')),
                ('diets_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weight_control.diets_list')),
                ('doctor_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='weight_control.doctor_profile')),
                ('preparats_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weight_control.preparats_list')),
            ],
        ),
        migrations.CreateModel(
            name='Pacient_reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField(blank=True, default=datetime.date.today)),
                ('weight_today', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pacient_profile_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='weight_control.pacient_profile')),
                ('symptoms_list', models.ManyToManyField(to='weight_control.symptoms_list')),
            ],
        ),
    ]
