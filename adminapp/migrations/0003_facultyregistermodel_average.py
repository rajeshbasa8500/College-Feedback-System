# Generated by Django 4.0.5 on 2022-11-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentregistermodel_student_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultyregistermodel',
            name='average',
            field=models.IntegerField(help_text='average', null=True),
        ),
    ]
