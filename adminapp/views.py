from email.headerregistry import Address
from fileinput import close
from re import A
from wsgiref.util import request_uri
from django.shortcuts import redirect, render
from regex import D
from adminapp.models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.crypto import get_random_string
from collegefeedback.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
import statistics

from studentapp.models import StudentFacultyfeedbackModel, StudentHostelfeedbackModel, StudentTransportfeedbackModel
from django.db.models import Avg,Sum,Count

# Create your views here.
def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if email == "admin" and password == "admin":
            messages.info(request, 'Login Successfully.')
            return redirect("admin_dashboard")
        else:
            messages.error(request,"Invalid EmailID or Password")
            return redirect("admin_login")
    return render(request, 'main/admin-login.html')


def admin_logout(request):
    # messages.info(request, 'Logout Successfully.')
    return redirect('index')


def admin_dashboard(request):
    a= FacultyRegisterModel.objects.count()
    b= StudentRegisterModel.objects.count()
    c= Hostel_RegisterModel.objects.count()
    d= TransportRegisterModel.objects.count()
    e=a+b+c+d
    f= StudentFacultyfeedbackModel.objects.count()
    g= StudentHostelfeedbackModel.objects.count()
    i=StudentTransportfeedbackModel.objects.count()
    
    print(e)
 
    return render(request, 'admin/admin-dashboard.html',{'h':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'i':i})


def admin_add_faculty(request):
    if request.method == "POST" and request.FILES['fphoto']:
        faculty_name = request.POST['facultyname']
        faculty_subject = request.POST['subject']
        faculty_gender = request.POST['gender']
        faculty_email = request.POST['email']
        chars = 'abcdefghijklmnopqrstuvwxyz098764321'
        faculty_password = get_random_string(6, chars)
        print(faculty_password)
        faculty_mobileno = request.POST['mobileno']
        faculty_address = request.POST['address']
        f_photo = request.FILES['fphoto']
        faculty_register = FacultyRegisterModel.objects.create(faculty_name=faculty_name, faculty_subject=faculty_subject, faculty_gender=faculty_gender,
                                                               faculty_email=faculty_email, faculty_mobileno=faculty_mobileno,  faculty_password=faculty_password, faculty_address=faculty_address, faculty_photo=f_photo)

        html_content = "<br/>Dear Faculty, <br/>   Your Login Credentials are generated <b> <br> Username: </b> " + \
            str(faculty_email) + "<br> <b>Passwod: </b> " + str(faculty_password) + \
            "<br> from Collegefeedaback system.  <br>  Thank You For Your Registration."
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [faculty_register.faculty_email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(
            "Account Registered Status", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        print(faculty_email)
        if msg.send():
            print("Sent")
        print('your success')
        messages.info(request,"Faculty Added Successfully")
        return redirect("admin_dashboard")      
    return render(request, 'admin/admin-add-faculty.html')


def admin_manage_faculty(request):
    a = FacultyRegisterModel.objects.all()
    return render(request, 'admin/admin-manage-faculty.html', {'a': a})


def admin_update_faculty(request, id):
    a = FacultyRegisterModel.objects.get(faculty_id=id)
    b = FacultyRegisterModel.objects.all()
    data = get_object_or_404(FacultyRegisterModel, faculty_id=id)

    if request.method == 'POST':
        faculty_name = request.POST['facultyname']
        faculty_subject = request.POST['subject']
        faculty_gender = request.POST['gender']
        faculty_email = request.POST['email']
        faculty_mobileno = request.POST['mobileno']
        faculty_address = request.POST['address']
        #faculty_photo = request.FILES['picture']
        print(faculty_mobileno)

        data.faculty_name = faculty_name
        data.faculty_subject = faculty_subject
        data.faculty_gender = faculty_gender
        data.faculty_email = faculty_email
        data.faculty_mobileno = faculty_mobileno
        data.faculty_address = faculty_address

        data.save(update_fields=['faculty_name', 'faculty_subject', 'faculty_gender',
                                 'faculty_email', 'faculty_mobileno', 'faculty_address'])
        messages.info(request, 'Updated Successfully.')
        data.save()
        messages.info(request,"Updated Successfully")
        return redirect('admin_update_faculty', id=id)
    return render(request, 'admin/admin-update-faculty.html', {'f': a , 'b':b})


def admin_add_student(request):
    if request.method == 'POST' and request.FILES['sphoto']:
        student_name = request.POST['studentname']
        student_branch = request.POST['branch']
        student_gender = request.POST['gender']
        student_mobileno = request.POST['mobileno']
        student_email = request.POST['email']
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        student_password = get_random_string(6, chars)
        print(student_password)
        chars = '01234567899876543210112233445566778899'
        student_otp = get_random_string(4, chars)
        print(student_otp)
        student_address = request.POST['address']
        student_photo = request.FILES['sphoto']
        
        student_register = StudentRegisterModel.objects.create(student_name=student_name, student_branch=student_branch, student_gender=student_gender, student_mobileno=student_mobileno,
                                                               student_email=student_email,  student_password=student_password, student_otp=student_otp, student_address=student_address, student_photo=student_photo)

        html_content = "<br/>Hi Dear Student, <br/>   Your Login Credentials are generated <b> <br> Username: </b> " + \
            str(student_email) + "<br> <b>Passwod: </b> " + str(student_password) + \
            "<br> from Collegefeedaback system.  <br>  Thank You For Your Registration."
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [student_register.student_email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(
            "Account Registered Status", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        print(student_email)
        # if msg.send():
        #     print("Sent")
        # print('your success')
        messages.info(request,"Student Added Successfully")
        return redirect("admin_dashboard")
    else:
        return render(request, 'admin/admin-add-student.html')


def admin_manage_student(request):
    b = StudentRegisterModel.objects.all()
    return render(request, 'admin/admin-manage-student.html', {'b': b})


def admin_update_student(request, id):
    b = StudentRegisterModel.objects.get(student_id=id)
    g = StudentRegisterModel.objects.all()
    
    data = get_object_or_404(StudentRegisterModel, student_id=id)
    if request.method == 'POST':
        student_name = request.POST['studentname']
        student_branch = request.POST['branch']
        student_gender = request.POST['gender']
        student_mobileno = request.POST['mobileno']
        student_email = request.POST['email']
        student_address = request.POST['address']
        #student_photo = request.FILES['sphoto']

        data.student_name = student_name
        data.student_branch = student_branch
        data.student_gender = student_gender
        data.student_mobileno = student_mobileno
        data.student_email = student_email
        data.student_address = student_address

        data.save(update_fields=['student_name', 'student_branch', 'student_gender',
                                 'student_mobileno', 'student_email', 'student_address'])
        messages.info(request, 'Updated Successfully.')
        data.save()
        messages.info(request,"Updated Successfully")
        return redirect('admin_update_student', id=id)
    return render(request, 'admin/admin-update-student.html', {'f': b,'g':g})


def admin_add_hostel(request):
    if request.method == 'POST':
        hostel_name = request.POST['hostelname']
        hostel_category = request.POST['hosteltype']
        hostel_mobileno = request.POST['mobileno']
        hostel_ac = request.POST['ac']
        hostel_email = request.POST['email']
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        hostel_password = get_random_string(6, chars)
        print(hostel_password)
        address = request.POST['address']
        hostel_register = Hostel_RegisterModel.objects.create(hostel_name=hostel_name,  hostel_category=hostel_category,
                                                              hostel_mobileno=hostel_mobileno,  hostel_ac=hostel_ac,  hostel_email=hostel_email,  hostel_password=hostel_password,  hostel_address=address)
        html_content = "<br/>Hi Dear Hostel Owner, <br/>   Your Login Credentials are generated <b> <br> hostelemail: </b> " + \
            str(hostel_email) + "<br> <b>Passwod: </b> " + str(hostel_password) + \
            "<br> from Collegefeedaback system.  <br>  Thank You For Your Registration."
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [hostel_register.hostel_email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(
            "Account Registered Status", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        print(hostel_email)
        if msg.send():
            print("Sent")
        print('your success')
        messages.info(request,"Hostel Added Successfully")
        return redirect("admin_dashboard")
    else:
        #messages.error(request,"Please fill above Details")
        return render(request, 'admin/admin-add-hostel.html')


def admin_manage_hostel(request):
    c = Hostel_RegisterModel.objects.all()
    return render(request, 'admin/admin-manage-hostel.html', {'c': c})


def admin_update_hostel(request, id):
    c = Hostel_RegisterModel.objects.get(hostel_id=id)
    if request.method == 'POST':
        hostel_name = request.POST['hostelname']
        hostel_category = request.POST['hosteltype']
        hostel_mobileno = request.POST['mobileno']
        hostel_ac = request.POST['ac']
        hostel_email = request.POST['email']
        hostel_address = request.POST['address']

        data = get_object_or_404(Hostel_RegisterModel, hostel_id=id)
        data.hostel_name = hostel_name
        data.hostel_category = hostel_category
        data.hostel_mobileno = hostel_mobileno
        data.hostel_ac = hostel_ac
        data.hostel_email = hostel_email
        data.hostel_address = hostel_address
        data.save(update_fields=['hostel_name', 'hostel_mobileno',
                                 'hostel_ac', 'hostel_email', 'hostel_address', 'hostel_category'])
        data.save()
        messages.info(request, 'Updated Successfully.')
        return redirect('admin_update_hostel', id=id)
    return render(request, 'admin/admin-update-hostel.html', {'f': c})


def admin_add_transport(request):
    if request.method == 'POST':
        vechicle_id = request.POST['vechicleid']
        vechicle_type = request.POST['vechicletype']
        driver_name = request.POST['drivername']
        route = request.POST['route']
        mobile_no = request.POST['mobileno']
        email = request.POST['email']
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        password = get_random_string(6, chars)
        print(password)
        transport_register = TransportRegisterModel.objects.create(
            vechicle_id=vechicle_id, vechicle_type=vechicle_type, driver_name=driver_name, route=route, mobile_no=mobile_no, email=email, password=password)
        html_content = "<br/>Hi Dear Hostel Owner, <br/>   Your Login Credentials are generated <b> <br> hostelemail: </b> " + \
            str(email) + "<br> <b>Passwod: </b> " + str(password) + \
            "<br> from Collegefeedaback system.  <br>  Thank You For Your Registration."
        from_mail = DEFAULT_FROM_EMAIL
        to_mail = [transport_register.email]
        # if send_mail(subject,message,from_mail,to_mail):
        msg = EmailMultiAlternatives(
            "Account Registered Status", html_content, from_mail, to_mail)
        msg.attach_alternative(html_content, "text/html")
        print(email)
        if msg.send():
            print("Sent")
        print('your success')
        messages.info(request,"Transport Added Successfully")
        return redirect("admin_dashboard")
    else: 
        #messages.error(request,"Please fill above Details")
        return render(request, 'admin/admin-add-transport.html')


def admin_manage_transport(request):
    d = TransportRegisterModel.objects.all()
    return render(request, 'admin/admin-manage-transport.html', {'d': d})


def admin_update_transport(request, id):
    d = get_object_or_404(TransportRegisterModel, transport_id=id)
    print(d.vechicle_id)
    if request.method == 'POST':
        vechicle_id = request.POST['vechicleid']
        vechicle_type = request.POST['vechicletype']
        driver_name = request.POST['drivername']
        route = request.POST['route']
        mobile_no = request.POST['mobileno']
        email = request.POST['email']

        data = get_object_or_404(TransportRegisterModel, transport_id=id)
        data.vechicle_id = vechicle_id
        data.vechicle_type = vechicle_type
        data.driver_name = driver_name
        data.route = route
        data.mobile_no = mobile_no
        data.email = email
        data.save(update_fields=['vechicle_id', 'vechicle_type',
                  'driver_name', 'route', 'mobile_no', 'email'])
        data.save()
        messages.info(request, 'Updated Successfully.')
        return redirect('admin_update_transport', id=id)
    return render(request, 'admin/admin-update-transport.html', {'f': d})


def admin_faculty_feedback(request):
    feedback = StudentFacultyfeedbackModel.objects.all()
    return render(request, 'admin/admin-faculty-feedback.html', {'feedback': feedback})


def fine(request, id):
    accept = get_object_or_404(StudentFacultyfeedbackModel, faculty_id=id)
    demo = "fine"
    accept.status = demo
    accept.save(update_fields=['status'])
    accept.save()
    messages.info(request,"Feedback Sent Successfully")
    return redirect("admin_faculty_feedback")


def bad(request, id):
    accept = get_object_or_404(StudentFacultyfeedbackModel, faculty_id=id)
    demo = "bad"
    accept.status = demo
    accept.save(update_fields=['status'])
    accept.save()
    messages.info(request,"Feedback Deleted Successfully")
    return redirect("admin_faculty_feedback")


def admin_hostel_facilities_feedback(request):
    feedback = StudentHostelfeedbackModel.objects.all()

    return render(request, 'admin/admin-hostel-facilities-feedback.html', {'feedback': feedback})


def genuine(request, id):
    accept = get_object_or_404(StudentHostelfeedbackModel, hostel_id=id)
    demo = "genuine"
    accept.status = demo
    accept.save(update_fields=['status'])
    accept.save()
    messages.info(request,"Feedback Sent Successfully")
    return redirect("admin_hostel_facilities_feedback")


def fake(request, id):
    accept = get_object_or_404(StudentHostelfeedbackModel, hostel_id=id)
    demo = "fake"
    accept.status = demo
    accept.delete()
    messages.info(request,"Feedback Deleted Successfully")
    return redirect("admin_hostel_facilities_feedback")


def admin_transport_facilities_feedback(request):
    feedback = StudentTransportfeedbackModel.objects.all()

    return render(request, 'admin/admin-transport-facilities-feedback.html', {'feedback': feedback})


def real(request, id):
    accept = get_object_or_404(StudentTransportfeedbackModel, transport_id=id)
    demo = "real"
    accept.status = demo
    accept.save(update_fields=['status'])
    accept.save()
    messages.info(request,"Feedback Sent Successfully")
    return redirect("admin_transport_facilities_feedback")


def fraud(request, id):
    accept = get_object_or_404(StudentTransportfeedbackModel, transport_id=id)
    demo = "fraud"
    accept.status = demo
    accept.delete()
    messages.info(request,"Feedback Deleted Successfully")
    return redirect("admin_transport_facilities_feedback")


def admin_faculty_student_opinion(request, id):
    fed = StudentFacultyfeedbackModel.objects.filter(faculty_id=id)
    return render(request, 'admin/admin-faculty-student-opinion.html', {'fed': fed})


def admin_faculty_analysis(request):
    a = FacultyRegisterModel.objects.all()    
    return render(request, 'admin/admin-faculty-analysis.html',{'a':a})


def admin_hostel_analysis(request):
    vpositive= StudentHostelfeedbackModel.objects.filter(sentiment='Very Positive').count()
    vnegitive = StudentHostelfeedbackModel.objects.filter(sentiment='Very Negitive').count()
    positive = StudentHostelfeedbackModel.objects.filter(sentiment='Positive').count()
    negitive = StudentHostelfeedbackModel.objects.filter(sentiment='Negitive').count()
    neutral = StudentHostelfeedbackModel.objects.filter(sentiment='Neutral').count()
    return render(request, 'admin/admin-hostel-analysis.html',{'vpositive':vpositive,'vnegitive':vnegitive,'positive':positive,'negitive':negitive,'neutral':neutral})


def admin_transport_analysis(request):
    vpositive= StudentTransportfeedbackModel.objects.filter(sentiment='Very Positive').count()
    vnegitive = StudentTransportfeedbackModel.objects.filter(sentiment='Very Negitive').count()
    positive = StudentTransportfeedbackModel.objects.filter(sentiment='Positive').count()
    negitive = StudentTransportfeedbackModel.objects.filter(sentiment='Negitive').count()
    neutral = StudentTransportfeedbackModel.objects.filter(sentiment='Neutral').count()
    return render(request, 'admin/admin-transport-analysis.html',{'vpositive':vpositive,'vnegitive':vnegitive,'positive':positive,'negitive':negitive,'neutral':neutral})
