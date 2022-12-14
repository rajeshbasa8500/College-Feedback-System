from django.shortcuts import redirect, render
from django.contrib import messages
from adminapp.models import FacultyRegisterModel, Hostel_RegisterModel, StudentRegisterModel, TransportRegisterModel
from adminapp.models import TransportRegisterModel
from studentapp.models import StudentTransportfeedbackModel

# Create your views here.


def transport_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print(email)
        password = request.POST.get("password")
        print(password)
        try:

            trans = TransportRegisterModel.objects.get(email=email, password=password)
             
            request.session['vechicle_id'] = trans.vechicle_id
            messages.info(request, "Login Successfully.")
            return redirect("transport_dashboard")
        except Exception as e:
            print(e)
            messages.error(request, "Invalid EmailID or Password")
    return render(request, 'main/transport-login.html')


def transport_dashboard(request):
    a= FacultyRegisterModel.objects.count()
    b= StudentRegisterModel.objects.count()
    c= Hostel_RegisterModel.objects.count()
    d= TransportRegisterModel.objects.count()
    e=a+b+c+d
    return render(request, 'transport/transport-dashboard.html',{'h':a,'b':b,'c':c,'d':d,'e':e})


def transport_view_feedback(request):
    feedback = StudentTransportfeedbackModel.objects.filter(vechicle_id=request.session['vechicle_id'],status='real')

    return render(request, 'transport/transport-view-feedback.html', {'feedback': feedback})


def transport_logout(request):
    return redirect('index')
