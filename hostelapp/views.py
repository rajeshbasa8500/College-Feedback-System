from django.shortcuts import redirect, render
from django.contrib import messages
from adminapp.models import Hostel_RegisterModel
from adminapp.models import FacultyRegisterModel, Hostel_RegisterModel, StudentRegisterModel, TransportRegisterModel
from studentapp.models import  StudentHostelfeedbackModel

# Create your views here.
def hostel_login(request):
    if request.method == "POST":
        print('post')
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            host = Hostel_RegisterModel.objects.get( hostel_email=email, hostel_password=password)
            request.session['hostel_name'] = host.hostel_name
            messages.info(request, "Login Successfully.") 
            return redirect("hostel_dashboard")
        except:
            print("error")
            messages.error(request, "Invalid EmailID or Password")
    return render(request, 'main/hostel-login.html ')


def hostel_dashboard(request):
    a= FacultyRegisterModel.objects.count()
    b= StudentRegisterModel.objects.count()
    c= Hostel_RegisterModel.objects.count()
    d= TransportRegisterModel.objects.count()
    e=a+b+c+d
    return render(request, 'hostel/hostel-dashboard.html',{'h':a,'b':b,'c':c,'d':d,'e':e})


def hostel_view_feedback(request):
    feedback = StudentHostelfeedbackModel.objects.filter( hostel_name=request.session['hostel_name'], status='genuine')

    return render(request, 'hostel/hostel-view-feedback.html', {'feedback': feedback})


def hostel_logout(request):
    return redirect('index')
