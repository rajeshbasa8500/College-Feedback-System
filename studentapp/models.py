from email.encoders import encode_base64
from encodings.utf_8 import encode
from django.db import models

from adminapp.models import FacultyRegisterModel, StudentRegisterModel

# Create your models here.
class StudentFacultyfeedbackModel(models.Model):
      faculty_id = models.AutoField(primary_key=True)
      fstudent_details = models.ForeignKey(StudentRegisterModel,models.PROTECT,null=True)
      faculty_name = models.CharField(help_text='faculty_name',max_length=50)
      faculty_subject = models.CharField(help_text='faculty_subject',max_length=20)
      ffeedback = models.CharField(help_text='ffeedback',max_length=50)
      status = models.CharField(help_text='status',max_length=50,default='pending')
      passion_and_enthusiasm_to_teach = models.IntegerField(help_text='passion_and_enthusiasm_to_teach',null=True)
      subject_knowledge = models.IntegerField(help_text='subject_knowledge',null=True)
      clarity_and_emphasis_on_concept = models.IntegerField(help_text='clarity_and_emphasis_on_concept',null=True)
      motivation_and_inspiration_the_student = models.IntegerField(help_text='motivation_and_inspiration_the_student',null=True)
      creating_interest_in_subject = models.IntegerField(help_text='creating_interest_in_subject',null=True)
      quality_of_illustrative_example=models.IntegerField(help_text='quality_of_illustrative_example',null=True)
      regularity_punctuality_and_uniform_coverage_of_syllabus=models.IntegerField(help_text='regularity_punctuality_and_uniform_coverage_of_syllabus',null=True)
      discipline_and_control_over_the_class = models.IntegerField(help_text='discipline_and_control_over_the_class',null=True)
      promoting_student_thinking=models.IntegerField(help_text='promoting_student_thinking',null=True)
      encouraging_and_student_interation=models.IntegerField(help_text='encouraging_and_student_interation',null=True)
      sentiment = models.CharField(help_text='sentiment',max_length=80,null=True)
      
      class Meta:
          db_table='studentfacultyfeeback_details'
        
class StudentHostelfeedbackModel(models.Model):
     hostel_id = models.AutoField(primary_key=True)
     student_details = models.ForeignKey(StudentRegisterModel,models.PROTECT,null=True)
     hostel_name = models.CharField(help_text='hostel_name',max_length=50)
     hfeedback = models.CharField(help_text='hfeedback',max_length=50)
     status = models.CharField(help_text='status',max_length=50,default='pending')
     sentiment = models.CharField(help_text='sentiment',max_length=80,null=True)
     class Meta:
         db_table='studenthostelfeeback_details'

class StudentTransportfeedbackModel(models.Model):
     transport_id = models.AutoField(primary_key=True)
     tstudent_details = models.ForeignKey(StudentRegisterModel,models.PROTECT,null=True)
     vechicle_id = models.CharField(help_text='vechicle_id',max_length=230,null=True)
     route = models.CharField(help_text='route',max_length=50,null=True)
     tfeedback = models.CharField(help_text='tfeedback',max_length=50)
     status = models.CharField(help_text='status',max_length=50,default='pending')
     sentiment = models.CharField(help_text='sentiment',max_length=80,null=True)
     class Meta:
         db_table='studenttransportfeeback_details'


      
             
         

              


   