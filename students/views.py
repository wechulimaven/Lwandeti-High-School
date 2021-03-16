from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from students.models import *
from .forms import HostelForm

def form_two(request):
    try:
        form_qs = FormClass.objects.get(formname__iexact='Form Two')
        
        student_qs = Student.objects.filter(form_class = form_qs)
        context = {'form_qs' : form_qs,
            'student_qs' : student_qs}        
        return render(request, 'student/form.html', context)
    except:
        messages.warning(request, f'No Form Two Student found')
        return redirect('students:all_student')

def form_three(request):
    try:
        form_qs = FormClass.objects.get(formname__iexact='Form Three')
        
        student_qs = Student.objects.filter(form_class = form_qs)
        context = {'form_qs' : form_qs,
            'student_qs' : student_qs}        
        return render(request, 'student/form.html', context)
    except:
        messages.warning(request, f'No Form Three Student found')
        return redirect('students:all_student')

def form_four(request):
    try:
        form_qs = FormClass.objects.get(formname__iexact='Form Four')
        
        student_qs = Student.objects.filter(form_class = form_qs)
        context = {'form_qs' : form_qs,
            'student_qs' : student_qs}        
        return render(request, 'student/form.html', context)
    except:
        messages.warning(request, f'No Form Four Student found')
        return redirect('students:all_student')
    
def boarding_students(request):
    bording = StudentBoarding.objects.all()
    student_qs = Student.objects.all()
    
    print(bording)
    
    context= {'bording': bording,
              'student_qs' : student_qs}
    return render(request, 'students/studentboarding.html', context)

def add_hostels(request):
    hostel_qs = Hostels.objects.all()
    form = HostelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        
        message.success(request, f'Hostel added Successfully')
        return redirect('students:boarding_students')
    else:
        message.warning(request, f'Please fill all the required fields correctly')
        return redirect('students:add_hostels')
    return render(request, 'students/add_hostels.html')

