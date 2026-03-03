from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import forms
from . import models


# Create your views here.
def create(request):
    
    if request.method == "POST":
        form = forms.StudentForm(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return HttpResponse("Student object create successfully.")

    else:
        form = forms.StudentForm()

    return render(request, 'student/create.html', {'form':form})


def student_list(request):
    # if request.method == 'GET':
    student = models.Student.objects.all()
    return render(request,'student/student_list.html', {'Students': student})

def update_student(request,id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)
    return render(request, 'student/update_student.html', {'form':form})

def home(request):
    return render(request, 'student/home.html')

def delet_student(request,id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return redirect('home')