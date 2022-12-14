from asyncio import transports
from io import TextIOBase
from django.shortcuts import redirect, render
from adminapp.models import FacultyRegisterModel, Hostel_RegisterModel, StudentRegisterModel, TransportRegisterModel
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from studentapp.models import StudentFacultyfeedbackModel, StudentHostelfeedbackModel, StudentTransportfeedbackModel
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import statistics
import requests
from django.db.models import Avg 


# Create your views here.


def student_login(request):
    if request.method == "POST":
        print('post')
        email = request.POST.get("email")
        print(email)
        password = request.POST.get("password")
        print(password)

        try:
            stus = StudentRegisterModel.objects.get(student_email=email, student_password=password)
            request.session['student_id'] = stus.student_id
            print(stus)
            print(stus.student_id)
            request.session['student_id'] = stus.student_id
            stus =StudentRegisterModel.objects.get()
            otp = stus.student_otp
            print(otp)
            url = "https://www.fast2sms.com/dev/bulkV2"
            # create a dictionary
            my_data = {'sender_id': 'FSTSMS', 
                        'message': 'Welcome to CloudHost, your verification OPT is '+str(otp)+ 'Thanks for request of OTP.', 
                        'language': 'english', 
                        'route': 'q', 
                        'numbers': 8500570538,
            }

            # create a dictionary
            headers = {
                'authorization': 'Ns8H1mKg294AjeBz5DMxLhPaZrbFR7tfpk3EX6wYJWUqd0noiGlHUTm1nDyEaCpx38R45MtKJg9kG6iB',
                'Content-Type': "application/x-www-form-urlencoded",
                'Cache-Control': "no-cache"
            }
            # make a post request
            response = requests.request("POST",
                                        url,
                                        data = my_data,
                                        headers = headers)
            # print the send message
            print(response.text)
            # return redirect('student_otp')
            ###*************SMS OTP********************####

            # messages.success(request,'Account Created Successfully!')
            
            
            messages.info(request, "Login Successfully.")
            return redirect("student_dashboard")

        except:
               messages.error(request, "Invalid EmailID or Password")
               return redirect('student_login')
    else:
        return render(request, 'main/student-login.html ')
               
#**************OTP*************************#
# def student_otp(request):        
#     if request.method == "POST":
#         otp = request.POST.get('otp')
#         try:
#             check = StudentRegisterModel.objects.get(student_otp=otp)
#             request.session['student_id']=check.student_id
#             p=check.student_otp
#             if p == otp:
#                 messages.info(request,'Login Successfully!')
#                 return redirect('student_dashboard')
#         except:
#             messages.error(request,'The OTP you entered is incorrect.Please try again.')
#             print('The OTP you entered is incorrect.Please try again.')
#             return redirect('student_otp')
#     return render(request,'student/student-otp.html')


def student_dashboard(request):
    a = FacultyRegisterModel.objects.count()
    b = StudentRegisterModel.objects.count()
    c = Hostel_RegisterModel.objects.count()
    d = TransportRegisterModel.objects.count()
    e = a+b+c+d
    return render(request, 'student/student-dashboard.html', {'h': a, 'b': b, 'c': c, 'd': d, 'e': e})


def student_my_profile(request):
    stu_id = request.session["student_id"]
    # print(f"id: {id}")
    #stu_id = 1
    # print("functioncalled")
    # print(student_id)
    j = StudentRegisterModel.objects.get(student_id=stu_id)
    obj = get_object_or_404(StudentRegisterModel, student_id=stu_id)

    if request.method == 'POST':
        student_name = request.POST['studentname']
        student_branch = request.POST['branch']
        student_gender = request.POST['gender']
        student_email = request.POST['email']
        student_mobileno = request.POST['mobileno']
        student_address = request.POST['address']

        if not request.FILES.get("sphoto", False):
            obj.student_name = student_name
            obj.student_branch = student_branch
            obj.student_gender = student_gender
            obj.student_email = student_email
            obj.student_mobileno = student_mobileno
            obj.student_address = student_address
            obj.save(update_fields=['student_name', 'student_branch', 'student_gender',
                     'student_email', 'student_mobileno', 'student_address'])
            obj.save()

        elif request.FILES.get("sphoto", False):
            s_photo = request.FILES["sphoto"]
            obj.student_name = student_name
            obj.student_branch = student_branch
            obj.student_gender = student_gender
            obj.student_email = student_email
            obj.student_mobileno = student_mobileno
            obj.student_address = student_address
            obj.student_photo = s_photo
            obj.save(update_fields=['student_name', 'student_branch', 'student_gender',
                     'student_email', 'student_mobileno', 'student_address', 'student_photo'])
            obj.save()
        messages.info(request, "Updated Successfully.")
    return render(request, 'student/student-my-profile.html', {'demo': j})


def student_faculty_choose(request):
    faculty = FacultyRegisterModel.objects.all()
    return render(request, 'student/student-faculty-choose.html', {'faculty': faculty})


def student_faculty_feedback(request,id):
    faculty_id = id
    id = request.session['student_id']
    studentfeedback = StudentRegisterModel.objects.get(student_id=id)
    demo = studentfeedback.student_name
    print(demo)
    print(id)
    p = FacultyRegisterModel.objects.get(faculty_id=faculty_id)
    print(p)
    fac=p.faculty_name
    avg=p.average
    if request.method == "POST":
        faculty_name = request.POST['facultyname']
        faculty_subject = request.POST['facultysubject']
        ffeedback = request.POST['feedback']
        if not request.POST.get('a'):
            return redirect('student_faculty_feedback', id=id)
        passion_and_enthusiasm_to_teach = request.POST['a']
        print(passion_and_enthusiasm_to_teach)
        if not request.POST.get('c'):
            return redirect('student_faculty_feedback', id=id)
        subject_knowledge = request.POST['c']
        if not request.POST.get('e'):
            return redirect('student_faculty_feedback', id=id)
        clarity_and_emphasis_on_concept = request.POST['e']
        if not request.POST.get('g'):
            return redirect('student_faculty_feedback', id=id)
        motivation_and_inspiration_the_student = request.POST['g']
        if not request.POST.get('i'):
            return redirect('student_faculty_feedback', id=id)
        creating_interest_in_subject = request.POST['i']
        if not request.POST.get('b'):
            return redirect('student_faculty_feedback', id=id)
        quality_of_illustrative_example = request.POST['b']
        if not request.POST.get('d'):
            return redirect('student_faculty_feedback', id=id)
        regularity_punctuality_and_uniform_coverage_of_syllabus = request.POST['d']
        if not request.POST.get('f'):
            return redirect('student_faculty_feedback', id=id)
        discipline_and_control_over_the_class = request.POST['f']
        if not request.POST.get('h'):
            return redirect('student_faculty_feedback', id=id)
        promoting_student_thinking = request.POST['h']
        if not request.POST.get('j'):
            return redirect('student_faculty_feedback', id=id)
        encouraging_and_student_interation = request.POST['j']

        # text analysis
        analysis = TextBlob(ffeedback,analyzer=NaiveBayesAnalyzer())
        print(analysis.sentiment)
        
        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity > -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'

        studentfeedback = StudentFacultyfeedbackModel.objects.create(faculty_name=faculty_name, faculty_subject=faculty_subject,
                                                                     ffeedback=ffeedback, fstudent_details=studentfeedback,
                                                                     passion_and_enthusiasm_to_teach=passion_and_enthusiasm_to_teach,
                                                                     subject_knowledge=subject_knowledge,
                                                                     clarity_and_emphasis_on_concept=clarity_and_emphasis_on_concept,
                                                                     motivation_and_inspiration_the_student=motivation_and_inspiration_the_student,
                                                                     creating_interest_in_subject=creating_interest_in_subject,
                                                                     quality_of_illustrative_example=quality_of_illustrative_example,
                                                                     regularity_punctuality_and_uniform_coverage_of_syllabus=regularity_punctuality_and_uniform_coverage_of_syllabus,
                                                                     discipline_and_control_over_the_class=discipline_and_control_over_the_class,
                                                                     promoting_student_thinking=promoting_student_thinking,
                                                                     encouraging_and_student_interation =encouraging_and_student_interation, sentiment=sentiment)
        a = StudentFacultyfeedbackModel.objects.filter(faculty_name=fac).aggregate(Avg('passion_and_enthusiasm_to_teach'),Avg('subject_knowledge'),Avg('clarity_and_emphasis_on_concept'),Avg('motivation_and_inspiration_the_student'),Avg('creating_interest_in_subject'),Avg('quality_of_illustrative_example'),Avg('regularity_punctuality_and_uniform_coverage_of_syllabus'),Avg('discipline_and_control_over_the_class'),Avg('promoting_student_thinking'),Avg('encouraging_and_student_interation'))
        # a = a[['passion_and_enthusiasm_to_teach'],['subject_knowledge'],['clarity_and_emphasis_on_concept'],['motivation_and_inspiration_the_student'],['creating_interest_in_subject'],['quality_of_illustrative_example'],['regularity_punctuality_and_uniform_coverage_of_syllabus'],['discipline_and_control_over_the_class'],['promoting_student_thinking'],['encouraging_and_student_interation']]
        # a=round(a)
        print(a,'kfav')
        b=sum(a.values())
        # b=round(b)
        print(b)
        c=b/10
        c=round(c)
        print(c)
        p.average=c
        p.save(update_fields=['average'])
        p.save()
        # print(student_feedback)
        messages.info(request, "Feedback sent Successfully.")
        return redirect("student_dashboard")

    return render(request, 'student/student-faculty-feedback.html', {'i': p})


def student_hostel_feedback(request):
    student_id = request.session['student_id']
    student = StudentRegisterModel.objects.get(student_id=student_id)
    demo = student.student_name
    print(demo)
    s = Hostel_RegisterModel.objects.all()
    if request.method == "POST":
        hostel_name = request.POST['hostelname']
        hfeedback = request.POST['feedback']
        # text analysis
        analysis = TextBlob(hfeedback)

        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'

        student = StudentHostelfeedbackModel.objects.create(
            student_details=student, hostel_name=hostel_name, hfeedback=hfeedback, sentiment=sentiment)
        messages.info(request, "Feedback sent Successfully.")
        return redirect("student_dashboard")
    return render(request, 'student/student-hostel-feedback.html', {'s': s})


def student_transport_choose(request):
    transport = TransportRegisterModel.objects.all()
    return render(request, 'student/student-transport-choose.html', {'transport': transport})


def student_transport_feedback(request, id):
    # student_id=request.session['student_id']
    # stransport=StudentRegisterModel.objects.get(student_id=student_id)
    # demo=stransport.student_name
    # print(demo)
    # v = TransportRegisterModel.objects.all()
    transport_id = id
    id = request.session['student_id']
    studentfeedback = StudentRegisterModel.objects.get(student_id=id)
    demo = studentfeedback.student_name
    print(demo)
    print(id)
    v = TransportRegisterModel.objects.filter(transport_id=transport_id)
    print(v)
    if request.method == "POST":
        vechicle_id = request.POST['vechicleid']
        route = request.POST['route']
        tfeedback = request.POST['feedback']
        # text analysis
        analysis = TextBlob(tfeedback)

        sentiment = ''
        if analysis.polarity >= 0.5:
            sentiment = 'Very Positive'
        elif analysis.polarity > 0 and analysis.polarity < 0.5:
            sentiment = 'Positive'
        elif analysis.polarity < 0 and analysis.polarity >= -0.5:
            sentiment = 'Negitive'
        elif analysis.polarity <= -0.5:
            sentiment = 'Very Negitive'
        else:
            sentiment = 'Neutral'
             
        StudentTransportfeedbackModel.objects.create(
            tstudent_details=studentfeedback, vechicle_id=vechicle_id, route=route, tfeedback=tfeedback, sentiment=sentiment)
        messages.info(request, "Feedback sent Successfully.")
        return redirect("student_dashboard")
    return render(request, 'student/student-transport-feedback.html', {'v': v})


def student_update_myprofile(request):
    return render(request, 'student/student-update-myprofile.html')
