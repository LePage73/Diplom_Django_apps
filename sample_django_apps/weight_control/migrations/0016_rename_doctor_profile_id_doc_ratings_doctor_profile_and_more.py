# Generated by Django 5.1.1 on 2024-10-21 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weight_control', '0015_rename_user_profile_assignment_pacient_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doc_ratings',
            old_name='doctor_profile_id',
            new_name='doctor_profile',
        ),
        migrations.RenameField(
            model_name='doc_ratings',
            old_name='patient_profile_id',
            new_name='pacient_profile',
        ),
    ]
