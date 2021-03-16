from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from staff.models import Designation, Formclass,TeachersProfileAttrib,ClassTeacherProfile, StudentProfileAttribute, StudentSubjects
from teachers.models import TeacherProfile
from students.models import Student, StudentBoarding


from staff.forms import StudentForm,StudentProfileAttributeForm, StudentSubjectsForm, StudentBoardingForm

def all_student(request, category_slug=None):
    form_class = None
    
    class_qs = Formclass.objects.all()
    stu_qs = Student.objects.all()
    if category_slug:
        form_class = get_object_or_404(Formclass, slug=category_slug)
        stu_qs = stu_qs.filter(form_class=form_class)
    context = {
        'form_class' :form_class,
        'class_qs' : class_qs,
        'stu_qs' : stu_qs
    }
    return render(request, "staff/all_students.html", context)

def all_teachers(request):
    teachers_qs = TeacherProfile.objects.all()
    TeachersProfileAttrib_qs = TeachersProfileAttrib.objects.all()
    dept_qs = Designation.objects.all()
    
    context = {'teachers_qs':teachers_qs,
               'TeachersProfileAttrib_qs':TeachersProfileAttrib_qs,
               'dept_qs':dept_qs}  
    return render(request, 'staff/all_teachers.html', context)

def add_student(request):
    context = {}
    student = Student.objects.all()
    studentform = StudentForm(request.POST or None, request.FILES or None)
    context = {
        'student': student,
        'studentform': studentform        
    }
    if request.method == 'POST':        
        if studentform.is_valid():
            adm = studentform.cleaned_data.get('admission_number')
            board = studentform.cleaned_data.get('boarding')
            obj = studentform.save(commit=False)
            
            exist_student = Student.objects.filter(admission_number=adm)
            
            if exist_student.count() == 1:
                exist_student = exist_student.first()
                messages.warning(request, f'Student {adm} Already exists !')
                return redirect('staff:all_students')
                
            # obj.boarding = request.POST['boarding']
            # obj.form_name_id = request.POST['form_name_id']
            # if board == True:
            #     boarding_qs = StudentBoarding.objects.all()
            #     StudentBoarding.objects.create(
            #         student = request.POST['student'],
            #         hostel = request.POST['hostel']
            #     )
            #     obj.save()
            #     boarding_qs = StudentBoarding.objects.all()                
            #     form = StudentBoardingForm(request.POST or None)
            #     context = {'boarding_qs':boarding_qs,
            #                'form':form}
            #     if form.is_valid():
            #         objec = form.save(commit = False)
            #         # objec.student_id = request.POST['student_id']
            #         # objec.hostel_id = request.POST['hostel_id']
            #         # host = form.cleaned_data.get('hostel')
            #         objec.save()                    
            #     # obj.save()
            #         messages.success(request, f'Student {adm} was admitted succesfuly and assigned  Hostel')
            #         return redirect("students:boarding_students")
            #     else:
            #         form = StudentBoardingForm()
            #         messages.warning(request, f'Student {adm} NOT ADMITTED fill form correctly')
            #         context['form'] = form
            #     return render(request, 'staff/assign_hostel.html', context)
                
            obj.save()
            if board == False:          
                messages.success(request, f'Student {adm} Added Successfully !')
                return redirect('staff:all_students')
            else:
                messages.success(request, f'Add Students {adm} residence !')
                return redirect('staff:assign_hostel')
                # studentt = Student.objects.last()
                # student_id = set(studentt)
                # boarding_qs = StudentBoarding.objects.all()
                # # obj.user_id = set_user_id.id
                # StudentBoarding.objects.create(
                #     student = request.POST.get('student', student_id),
                #     hostel = request.POST['hostel']
                # )
                # messages.success(request, f'Student {adm} was admitted succesfuly and assigned  Hostel')
                # return redirect("students:boarding_students")

            # return render(request, 'staff/assign_hostel.html', context)
                
        else:
            studentform = StudentForm()
            messages.warning(request, f'Student {adm} NOT ADMITTED fill form correctly !')
            context['studentform'] = studentform
    return render(request, 'staff/admission.html', context)
    # return render(request, 'staff/add_student.html', context)
    
def assign_hostel(request):
    context={}
    teachers_qs = TeacherProfile.objects.filter(id=request.user.id)
    boarding_qs = StudentBoarding.objects.all()
    boarding_student_qs = Student.objects.filter(boarding=True)
 
    context = {'boarding_qs':boarding_qs,
               'boarding_student_qs' : boarding_student_qs,
               'teachers_qs' : teachers_qs}
    if request.method == 'POST':
        form = StudentBoardingForm(request.POST or None)
        context['form'] = form
        if form.is_valid():
            objec = form.save(commit = False)
            # objec.student_id = request.POST['student_id']
            # objec.hostel_id = request.POST['hostel_id']
            host = form.cleaned_data.get('hostel')
            student= form.cleaned_data.get('student_id')
            
            qs = StudentBoarding.objects.filter(id=student)
            if qs.count() == 1:
                qs = qs.first()                
                messages.warning(request, f'Student  already exists or resides in a Hostel')
                return redirect("students:boarding_students")                       
            
            objec.save()
            messages.success(request, f'Student was admitted succesfuly and assigned  Hostel')
            return redirect("students:boarding_students")
        
    else:
        form = StudentBoardingForm()
        messages.warning(request, f'Student Not Assigned A Hostel !')
        context['form'] = form
    return render(request, 'staff/assign_hostel.html', context)

def edit_student(request, id):
    context = {}
    student_qs = Student.objects.get(pk=id)
    formclass_qs = Formclass.objects.all()
    context['student_qs'] = student_qs
    context['formclass_qs'] = formclass_qs
    if request.method == 'POST':
        Student.objects.filter(pk=id).update(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            admission_number = request.POST['admission_number'],
            # reg_date = request.POST['reg_date'],
            form_class = request.POST['form_name'],
            gender = request.POST['gender'],
            parent_name = request.POST['parent_name'],
            parent_mobile_number = request.POST['parent_mobile_number'],
            dob = request.POST['dob'],
            email = request.POST['email'],
            address = request.POST['address'],
            # student_photo = request.FILES['student_photo'],
            
        )
        # adm = studentform.cleaned_data.get('admission_number')
        messages.success(request, f'Student Information Updated Successfully ')
        return redirect('staff:all_students')
    return render(request, 'staff/edit_student.html', context)

def delete_student(request):
    if request.method == 'POST':
        item = request.POST['id']
        deletestudent = Student.objects.get(id=item)
        deletestudent.delete()
        messages.success(request, f'Student Deleted Successfully')
        return redirect('staff:all_students')
    
# def add_student_subjects(request):
    
    