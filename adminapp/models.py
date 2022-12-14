from email.mime import image
from re import T
from django.db import models

# Create your models here.


class FacultyRegisterModel(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(help_text='faculty_name',max_length=50)
    faculty_subject = models.CharField(help_text='faculty_subject',max_length=20)
    faculty_gender = models.CharField(help_text='faculty_gender', max_length=10)
    faculty_email = models.CharField(help_text='faculty_email', max_length=30)
    faculty_password = models.CharField(help_text='faculty_password', max_length=30, null=True)
    faculty_mobileno = models.BigIntegerField(help_text='faculty_mobileno',null=True)
    faculty_address = models.CharField(help_text='faculty_address', max_length=20)
    faculty_photo = models.ImageField(null=True, blank=True)
    average = models.IntegerField(help_text='average',null=True)
    class Meta:
        db_table='faculty_details'
        

class StudentRegisterModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(help_text='student_name',max_length=50)
    student_branch = models.CharField(help_text='student_branch',max_length=20)
    student_gender = models.CharField(help_text='student_gender', max_length=10)
    student_mobileno = models.BigIntegerField(help_text='student_mobileno',null=True)
    student_email = models.CharField(help_text='student_email', max_length=30)
    student_password = models.CharField(help_text='student_password',max_length=18)
    student_otp = models.CharField(help_text='student_otp',max_length=18,null=True)
    student_address = models.CharField(help_text='student_address', max_length=20)
    student_photo = models.ImageField(null=True, blank=True)
    
    class Meta:
        db_table='student_details'
        

class Hostel_RegisterModel(models.Model):
    hostel_id = models.AutoField(primary_key=True)
    hostel_name = models.CharField(help_text='hostel_name',max_length=50)
    hostel_category = models.CharField(max_length=20)
    hostel_mobileno =  models.BigIntegerField(help_text='hostel_mobileno',null=True)
    hostel_ac= models.CharField(help_text='ac',max_length=10)
    hostel_email = models.CharField(help_text='hostel_email', max_length=30)
    hostel_password = models.CharField(help_text='hostel_password',max_length=18,null=True)
    hostel_address = models.CharField(help_text='hostel_address', max_length=20)
    
    class Meta:
        db_table='hostel_details'

 

class TransportRegisterModel(models.Model):
    transport_id = models.AutoField(primary_key=True)
    vechicle_id = models.CharField(help_text='vechicle_id',max_length=50,null=True)
    vechicle_type = models.CharField(help_text='vechicle_type',max_length=50,null=True)
    driver_name = models.CharField(help_text='driver_name', max_length=20, default="Rajesh",null=True)
    route = models.CharField(help_text='root', max_length=18,null=True)
    email = models.CharField(help_text='email', max_length=30)
    password = models.CharField(help_text='password',max_length=18,null=True)
    mobile_no = models.BigIntegerField(help_text='mobile_no',null=True)
    
    class Meta:
        db_table='transport_details'








