import email
from email import message
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render
from adminapp.models import FacultyRegisterModel
from adminapp.models import FacultyRegisterModel, Hostel_RegisterModel, StudentRegisterModel, TransportRegisterModel
from studentapp.models import StudentFacultyfeedbackModel
from django.contrib import messages

# Create your views here.
def faculty_login(request):
    if request.method == "POST":
        print('post')
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            facultee = FacultyRegisterModel.objects.get(faculty_email = email ,faculty_password = password)
            # print(facultee)
            # print(facultee.faculty_id)
            
            request.session['faculty_name']=facultee.faculty_name
            messages.info(request, "Login Successfully.")
            return redirect("faculty_dashboard")
        except:
            messages.error(request,"Invalid EmailID or Password")
    return render(request, 'main/faculty-login.html ')


def faculty_logout(request):
    # messages.info(request, "Logout Successfully.")
    return redirect('index')

def faculty_dashboard(request):
    a= FacultyRegisterModel.objects.count()
    b= StudentRegisterModel.objects.count()
    c= Hostel_RegisterModel.objects.count()
    d= TransportRegisterModel.objects.count()
    e=a+b+c+d
    return render(request, 'faculty/faculty-dashboard.html',{'h':a,'b':b,'c':c,'d':d,'e':e})

def faculty_my_profile(request):
    faculty_name = request.session["faculty_name"]
    j = FacultyRegisterModel.objects.filter(faculty_name=faculty_name)
    #obj=get_object_or_404(FacultyRegisterModel,faculty_id=faculty_id)
    obj = get_object_or_404(FacultyRegisterModel, faculty_name=faculty_name)
    if request.method == 'POST':
        faculty_name = request.POST['facultyname']
        faculty_subject = request.POST['subject']
        faculty_gender = request.POST['gender']
        faculty_email = request.POST['email']
        faculty_mobileno = request.POST['mobileno']
        faculty_address = request.POST['address']
       
        if not request.FILES.get("fpicture",False):
            # print("yes efffeg jfkdftjhkt")
            obj.faculty_name = faculty_name
            obj.faculty_subject = faculty_subject
            obj.faculty_gender = faculty_gender
            obj.faculty_email = faculty_email
            obj.faculty_mobileno = faculty_mobileno
            obj.faculty_address = faculty_address
            obj.save(update_fields=['faculty_name', 'faculty_subject', 'faculty_gender',
                                        'faculty_email', 'faculty_mobileno', 'faculty_address'])
            obj.save()
             
        elif request.FILES.get("fpicture",False):
            f_photo = request.FILES['fpicture']
            obj.faculty_name = faculty_name
            obj.faculty_subject = faculty_subject
            obj.faculty_gender = faculty_gender
            obj.faculty_email = faculty_email
            obj.faculty_mobileno = faculty_mobileno
            obj.faculty_address = faculty_address
            obj.faculty_photo = f_photo
            obj.save(update_fields=['faculty_name', 'faculty_subject', 'faculty_gender',
                                        'faculty_email', 'faculty_mobileno', 'faculty_address', 'faculty_photo'])
            obj.save()
           
           
        messages.info(request, 'Updated Successfully.')       
    
    return render(request, 'faculty/faculty-my-profile.html',{'demo':j})

def faculty_view_feedback(request):
    feedback = StudentFacultyfeedbackModel.objects.filter(faculty_name=request.session['faculty_name'], status='fine')
    return render(request, 'faculty/faculty-view-feedback.html', {'feedback': feedback})

def faculty_student_opinion(request,id):
    fed = StudentFacultyfeedbackModel.objects.filter(faculty_id=id)
    return render(request, 'faculty/faculty-student-opinion.html', {'fed':fed})

def faculty_update_myprofile(request):
    return render(request, 'faculty/faculty-update-myprofile.html')


