"""collegefeedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pip import main
import facultyapp

from mainapp import views as mainapp_views
from adminapp import views as adminapp_views
from facultyapp import views as facultyapp_views
from studentapp import views as studentapp_views
from hostelapp import views as hostelapp_views
from transportapp import views as transportapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp_views.index, name='index'),
    # path('',mainapp_views.index,name='faculty'),
    # path('',mainapp_views.index,name='student'),
    # path('',mainapp_views.index,name='hostel'),
    # path('',mainapp_views.index,name='transport'),

    # main

    # student
    path('student-login',studentapp_views.student_login,name='student_login'),

    path('student-dashboard',studentapp_views.student_dashboard,name='student_dashboard'),

    path('student-my-profile',studentapp_views.student_my_profile,name='student_my_profile'),
    
    path('student-faculty-choose',studentapp_views.student_faculty_choose,name='student_faculty_choose'),

    path('student_faculty_feedback/<int:id>/',studentapp_views.student_faculty_feedback,name='student_faculty_feedback'),

    path('student-hostel-feedback',studentapp_views.student_hostel_feedback,name='student_hostel_feedback'),
    
    path('student-transport-choose',studentapp_views.student_transport_choose,name='student_transport_choose'),

    path('student_transport_feedback/<int:id>/',studentapp_views.student_transport_feedback,name='student_transport_feedback'),

    path('student-update-myprofile',studentapp_views.student_update_myprofile,name='student_update_myprofile'),
    
    # path('student-otp',studentapp_views.student_otp,name='student_otp'),
    
    # faculty
    path('faculty-login',facultyapp_views.faculty_login,name='faculty_login'),

    path('faculty-logout',facultyapp_views.faculty_logout,name='faculty_logout'),

    path('faculty-dashboard',facultyapp_views.faculty_dashboard,name='faculty_dashboard'),

    path('faculty-my-profile',facultyapp_views.faculty_my_profile,name='faculty_my_profile'),

    path('faculty_student_opinion/<int:id>',facultyapp_views.faculty_student_opinion,name='faculty_student_opinion'),

    path('faculty-view-feedback',facultyapp_views.faculty_view_feedback,name='faculty_view_feedback'),


    # hostel
    path('hostel-login',hostelapp_views.hostel_login,name='hostel_login'),

    path('hostel-dashboard',hostelapp_views.hostel_dashboard,name='hostel_dashboard'),

    path('hostel-view-feedback',hostelapp_views.hostel_view_feedback,name='hostel_view_feedback'),
    
    path('hostel-logout',hostelapp_views.hostel_logout,name='hostel_logout'),


    # transport
    path('transport-login',transportapp_views.transport_login,name='transport_login'),

    path('transport-dashboard',transportapp_views.transport_dashboard,name='transport_dashboard'),

    path('transport-view-feedback',transportapp_views.transport_view_feedback,name='transport_view_feedback'),

    path('transport-logout',transportapp_views.transport_logout,name='transport_logout'),


    # admin
    path('admin-login',adminapp_views.admin_login,name='admin_login'),

    path('admin-logout',adminapp_views.admin_logout,name='admin_logout'),

    path('admin_dashboard',adminapp_views.admin_dashboard,name='admin_dashboard'),

    path('admin_add_faculty',adminapp_views.admin_add_faculty,name='admin_add_faculty'),

    path('admin_manage_faculty',adminapp_views.admin_manage_faculty,name='admin_manage_faculty'),

    path('admin_update_faculty/<int:id>/',adminapp_views.admin_update_faculty,name='admin_update_faculty'),

    path('admin_add_student',adminapp_views.admin_add_student,name='admin_add_student'),

    path('admin_manage_student',adminapp_views.admin_manage_student,name='admin_manage_student'),

    path('admin_update_student/<int:id>/',adminapp_views.admin_update_student, name='admin_update_student'),

    path('admin_add_hostel',adminapp_views.admin_add_hostel,name='admin_add_hostel'),

    path('admin_manage_hostel',adminapp_views.admin_manage_hostel,name='admin_manage_hostel'),

    path('admin_update_hostel/<int:id>/',adminapp_views.admin_update_hostel,name='admin_update_hostel'),

    path('admin_add_transport',adminapp_views.admin_add_transport,name='admin_add_transport'),

    path('admin_manage_transport',adminapp_views.admin_manage_transport,name='admin_manage_transport'),

    path('admin_update_transport/<int:id>/',adminapp_views.admin_update_transport,name='admin_update_transport'),

    path('admin_faculty_feedback',adminapp_views.admin_faculty_feedback,name='admin_faculty_feedback'),

    path('admin_hostel_facilities',adminapp_views.admin_hostel_facilities_feedback,name='admin_hostel_facilities_feedback'),

    path('admin_transport_facilities',adminapp_views.admin_transport_facilities_feedback,name='admin_transport_facilities_feedback'),

    path('admin_faculty_student_opinion/<int:id>/',adminapp_views.admin_faculty_student_opinion,name='admin_faculty_student_opinion'),

    path('admin_faculty_analysis',adminapp_views.admin_faculty_analysis,name='admin_faculty_analysis'),

    path('fine/<int:id>/',adminapp_views.fine, name='fine'),

    path('bad/<int:id>/',adminapp_views.bad, name='bad'),

    path('admin_hostel_analysis',adminapp_views.admin_hostel_analysis,name='admin_hostel_analysis'),

    path('genuine/<int:id>',adminapp_views.genuine, name='genuine'),

    path('fake/<int:id>',adminapp_views.fake, name='fake'),

    path('admin_transport_analysis',adminapp_views.admin_transport_analysis,name='admin_transport_analysis'),

    path('real/<int:id>',adminapp_views.real, name='real'),

    path('fraud/<int:id>',adminapp_views.fraud, name='fraud'),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
