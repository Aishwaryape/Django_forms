from django.shortcuts import render, redirect
from .forms import stuForm
from .forms import StudentForm
from .forms import EmployeeForm
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .functions.functions import handle_uploaded_file
from .forms import StudentForm


# Create your views here.
def myfun(request):
    return render(request, 'index.html')


def index(request):
    stu = stuForm()
    return render(request, "index.html", {'form': stu})


def index1(request):
    if request.method == 'POST':
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        student = StudentForm()
        return render(request, "index.html", {'form': student})


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form': form})


# Session
def setsession(request):
    request.session['sname'] = 'Aishwarya'
    request.session['semail'] = 'Aishwarya.sssit@gmail.com'
    return HttpResponse("session is set")


def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname + " " + studentemail)


# Cookies
def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('Aishwarya', 'Pendkar')
    return response


def getcookie(request):
    tutorial = request.COOKIES['Aishwarya']
    return HttpResponse("Name is : " + tutorial)
