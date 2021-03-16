from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .forms import (TeachersProfileForm, TeachersProfileAttribForm, 
                    UserLoginForm, UserRegisterForm,
                    StudentProfileAttributeForm, StudentSubjectsForm)
from .models import TeacherProfile, EducationStatus
from staff.models import Designation, TeachersProfileAttrib, StudentProfileAttribute, StudentSubjects, ClassTeacherProfile
from subjects.models import Subject, CompulsorySubjects
from students.models import Student

def login_teacher(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # str_relace = str.replace(username, '/', f'')
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, f'login was successful')
            return redirect('teachers:teacher_profile')
        else:
            messages.warning(request, f'login Error !!!! Provide Correct Username And Password')
            return redirect('teachers:login_teacher')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def add_student_subject(request):
    context = {}
    try:
        # profile_attr = StudentProfileAttribute.objects.get(classteacher_id = request.user.teacherprofile.id)
        profile_attr = StudentProfileAttribute.objects.get(classteacher_id = request.user.classteacherprofile.id)
        print(profile_attr)
        subjects = Subject.objects.filter(formclass_id = profile_attr.formclass)
        studentsubject_qs = StudentSubjects.objects.filter(classteacher_id = request.user.classteacherprofile.id)
        context = {'profile_attr':profile_attr,
                'subjects':subjects,
                'studentsubject_qs':studentsubject_qs}
        if request.method == 'POST':
                try:
                    obj = StudentSubjects.objects.get(
                        classteacher_id = request.user.classteacherprofile.id,
                        subjects_id = request.POST.get('subjects'),
                    )
                    messages.warning(request, f'Subject Already exist {request.user.username}')
                except StudentSubjects.DoesNotExist:
                    new_values = {}
                    new_values.update(
                        classteacher_id = request.user.classteacherprofile.id,
                        subjects_id = request.POST.get('subjects'),
                    )
                    obj = StudentSubjects(**new_values)
                    obj.save()
    except ObjectDoesNotExist:
        messages.warning(request, f'Sorry You aint a classteacher {request.user.username}')
        return redirect('teachers:teacher_profile')
    return render(request, 'teachers/subject.html', context)

#Display students Term and class
def student_profile_attrib(request):
    context = {}
    try:
        attrib_qs = StudentProfileAttribute.objects.all()
        classteacher = ClassTeacherProfile.objects.filter(id = request.user.id)
        
        context={'attrib_qs':attrib_qs,
                'classteacher':classteacher}
    except ObjectDoesNotExist:
        messages.warning(request, f'Sorry You aint a classteacher {request.user.username}')
        return redirect('teachers:teacher_profile') 
    return render(request, 'teachers/studentprofileattrib.html', context) 

#register students subjects depending on the term and class
def register_student_subject(request, id):
    context = {}
    profile_attr = StudentProfileAttribute.objects.get(pk=id)
    subjects = Subject.objects.filter(formclass_id = profile_attr.formclass)#in mind store the formclass id from subject
    # subjects = Subject.objects.all()
    studentsubject_qs = StudentSubjects.objects.filter(student_id = id)
    context = {'profile_attr':profile_attr,
            'subjects':subjects,
            'studentsubject_qs':studentsubject_qs}
    
    if request.method == 'POST':
        form = StudentSubjectsForm(request.POST or None) 
        if form .is_valid():
            std_id = request.POST['student']
            obj = form.save(commit=False)
            obj.classteacher_id = request.POST['classteacher']
            obj.student_id = request.POST['student']
            obj.subjects_id = request.POST['subjects']
            obj.save()
            return redirect('teachers:students_attributes')
        else:
            form = StudentSubjectsForm
            context = {'form':form}
    return render(request, 'teachers/register_student_subject.html', context)
    # return render(request, 'teachers/trial.html', context)

def student_subjects(request):
    context = {}
    studentsubject_qs = StudentSubjects.objects.all()
    classteacherprofile_qs = ClassTeacherProfile.objects.all()
    student_qs = Student.objects.all()
    subject_qs = Subject.objects.all()
    context = {'studentsubject_qs':studentsubject_qs,
               'classteacherprofile_qs':classteacherprofile_qs,
               'student_qs':student_qs,
               'subject_qs':subject_qs}
    return render(request, 'teachers/student_subject.html',context)
    # return render(request, 'teachers/subjects_list.html',context)    


def stuff_profile(request):
    context = {}
    # teacherprofile = TeacherProfile.objects.filter(user_id = request.user.id)
    return render(request, 'teachers/profile_detail.html', context)

def teacher_profile(request):
    context = {}
    try:
        profile_attr = TeachersProfileAttrib.objects.get(teacher_id = request.user.teacherprofile.id)
        # year_percentage = int(profile_attr.year_of_study)/4 * 100
        
        # student_subjects = StudentSubject.objects.filter(student_id = request.user.teacherprofile.id).count()
        # subjects = Subject.objects.filter(program=profile_attr.program).count()
        
        # context['subjects'] = subjects
        context['profile_attr'] = profile_attr
        # context['year_percentage'] = year_percentage
        # context['student_subjects'] = student_subjects
        
    except ObjectDoesNotExist:
        messages.warning(request, f'Register Your Attributes {request.user.username}')
        return redirect('teachers:teachers_profile_attribute')    
    return render(request, 'teachers/profile.html', context)


@staff_member_required(login_url='admin:login')
def add_teachers_profile(request):
    # try:
    #     profile_attr = HodProfile.objects.get(user = request.user.hodprofile.user)
    if request.method == 'POST':
        form = TeachersProfileForm(request.POST)
        if form.is_valid():
            id_number = form.cleaned_data.get('id_number')
            email_address = form.cleaned_data.get('first_name')
            email_to_save = f'{email_address}@gmail.com'
            
            user_qs = User.objects.filter(username=id_number)
            if user_qs.count() == 1:
                user = user_qs.first()
                # check if the student already exists
                # user = authenticate(username=adm_number,password=adm_number)
                # login(request, user)
                messages.warning(request, f'Student with Adm No. :{id_number}, already exist')
                return redirect('staff:teacher_profile')
            else:
                User.objects.create_user(
                    username = id_number,
                    email= email_to_save,
                    password = id_number,
                )
            
                # Authenticate the created student with the profile
                # user = authenticate(username=adm_number,password=adm_number)
                # login(request, user)
                set_user_id = User.objects.get(username=id_number)
                messages.success(request, f'{id_number} created successful')
                # save the StudentProfileForm with the current set user id
                obj = form.save(commit = False)
                obj.user_id = set_user_id.id
                obj.save()  
                return redirect('staff:teachers_profile_attribute')
        else:
            messages.success(request, f'login Error !!!! Provide Correct Username And Password')
            return redirect('staff:add_teachers_profile')
    else:
        form = TeachersProfileForm()
    return render(request, 'staff/addteachersprofile.html', {'form': form})
    # except ObjectDoesNotExist:
    #     return redirect('stuff:createhodprofile')

@staff_member_required(login_url='admin:login')   
@login_required(login_url='teachers:login_teacher')
def teachers_profile_attribute(request):
    try:
        profile_attr = TeachersProfileAttrib.objects.get(teacher_id = request.user.teacherprofile.id)
        return redirect('teachers:teachers_profile')
    except ObjectDoesNotExist:
        context = {}
        # subjects = Subject.objects.all()
        teacher_qs = TeacherProfile.objects.all()
        designations = Designation.objects.all()
        status_qs = EducationStatus.objects.all()
        context['designations'] = designations
        context['teacher_qs'] = teacher_qs
        if request.method == 'POST':
            form = TeachersProfileAttribForm(request.POST, request.FILES)
            # print(request.POST['subject'])
            if form.is_valid():
                obj = form.save(commit = False)
                # obj.teacher_id = request.user.teacherprofile.id
                obj.teacher_id = request.POST['teacher_id']
                obj.designation_id = request.POST['designation_id']
                # obj.subject = request.POST['subject']
                obj.save()
                messages.success(request, f'Profile Attribute for {request.user.username} was created successfuly!')
                # return redirect('staff:add_teachers_profile')
                return redirect('teachers:teachers_profile')  
            else:
                messages.warning(request, f'Fill the form Correctly {request.user.username}')
                return redirect('teachers:teachers_profile_attribute')  
        else:
            form = TeachersProfileAttribForm()
            context['form'] = form
    return render(request, 'teachers/profileattr.html', context)

def edit_teachers_profile_attribute(request):
    context={}

    try:
        profile_attr = TeachersProfileAttrib.objects.get(teacher_id = request.user.teacherprofile.id)
        # teacher_qs = TeacherProfile.objects.all()
        designations = Designation.objects.all()
        context = {'profile_attr':profile_attr,
                   'designations':designations}
        if request.method == 'POST':
            TeachersProfileAttrib.objects.update(
              mobile_number = request.POST['mobile_number'],
              designation = request.POST['designation'],
              gender = request.POST['gender'],
              dob = request.POST['dob'],
              address = request.POST['address'],
              educational_status = request.POST['educational_status'],
              joined_date = request.POST['joined_date'],
              profile_photo = request.FILES['profile_photo']     
                            
            )
            messages.success(request, f'Teachers Information Updated Successfully ')
            return redirect('staff:all_teachers')
        return render(request, 'teachers/edit_teachers.html', context)        
    except ObjectDoesNotExist:
        messages.warning(request, f'No Profile found Create Profile first {user.username} ')
        return redirect('teachers:teachers_profile_attribute')


def student_exam_shit(request):
    pass
def user_logout(request):
    logout(request)
    messages.warning(request, f'You Have logout !!!')
    return redirect('teachers:login_teacher')

