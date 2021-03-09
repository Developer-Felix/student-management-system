import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import CustomUser,Staffs,Courses,Student

def admin_home(request):
    return render(request, 'hod_template/home_content.html')

def AddStaff(request):
    return render(request, 'hod_template/add_staff_template.html')


def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allow")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=2)
            user.staffs.address = address
            user.save()
            # messages.success(request,"Successfully added Staff")
            messages.success(request,"Successfully added Staff")
            return HttpResponseRedirect("/add_staff")
            print("succcess")
        except:
            messages.error(request,"Failed to add Staff")
            return HttpResponseRedirect("/add_staff")
            print("succcess")

def add_course(request):
    return render(request, 'hod_template/add_course_template.html')

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        course = request.POST.get("course")
        try:
            course_model = Courses(course=course)
            course_model.save()
            messages.success(request,"Successfully added Course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request,"Failed to add Course")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(request, 'hod_template/add_student_template.html',{"courses":courses})






def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method not allow")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        session_start = request.POST.get("session_start")
        session_end = request.POST.get("session_end")
        course_id = request.POST.get("course")
        sex = request.POST.get("sex")
        try:
            user = CustomUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email, user_type=3)
            user.student.address = address
            course_obj = Courses.objects.get(id=course_id)
            user.student.course_id = course_obj
        # print(course_obj)
        # start_date = datetime.datetime.strptime(session_start,'%y-%m-%d').strftime('%Y-%m-%d')
        # end_date = datetime.datetime.strptime(session_end,'%y-%m-%d').strftime('%Y-%m-%d')

            user.student.session_start_year = session_start
            user.student.session_end_year = session_end
            user.student.gender = sex
            user.student.profile_pic = ""
            user.save()
            messages.success(request, "Successfully added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add Student")
            return HttpResponseRedirect("/add_student")