from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from staff.models import Designation, Formclass,ClassTeacherProfile, StudentProfileAttribute, StudentSubjects
from students.models import Student, StudentBoarding


class StudentForm(forms.ModelForm):
    """Form definition for StudentProfile."""
    # first_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'first_name', 'required': 'true'}))
    # last_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'last_name', 'required': 'true'}))
    # admission_number = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'id_number', 'required': 'true'}))
    # gender = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'gender','tabIndex': '-1', 
    #            'readonly': 'true', 'required': 'true'}))
    # parent_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'parent_name', 'required': 'true'}))
    # parent_mobile_number = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'parent_mobile_number', 'pattern': '-?[0-9]*(\.[0-9]+)?',  'required': 'true'}))
    # address = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'address', 'required': 'true'}))
    # email = forms.EmailField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'id_email', 'required': 'true'}))
    # dob = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'dateOfBirth',  'required': 'true'}))
    # student_photo = forms.FileField(widget=forms.FileInput(
    #     attrs={'class': 'dropzone','id': 'profile_photo', 'accept':'image/*', 'required': 'true'}))
    
    class Meta:
        """Meta definition for StudentProfileform."""

        model = Student
        fields = ['first_name','last_name','admission_number','form_name',
                  'gender','boarding','parent_name','parent_mobile_number',
                  'address','email','dob','student_photo']
        # def Boarding(self):
        #     if self.boarding == True:
        #         return redirect("staff:all_teachers") #change to student boarding function form
        #     else:
        #         return redirect("staff:add_student")
        
class StudentBoardingForm(forms.ModelForm):
    class Meta:
        model = StudentBoarding
        fields = ['student', 'hostel']
        
class ClassTeacherProfileForm(forms.ModelForm):
    """Form definition for StudentProfile."""
    formclass = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'formclass', 'required': 'true'}))
    year = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'year', 'required': 'true'}))
    
    class Meta:
        """Meta definition for StudentProfileform."""

        model = ClassTeacherProfile
        fields = ['formclass','year']
        
class StudentSubjectsForm(forms.ModelForm):
    """Form definition for StudentProfile."""
    student = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'student', 'required': 'true'}))
    subjects = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subjects', 'required': 'true'}))
    
    class Meta:
        """Meta definition for StudentProfileform."""

        model = StudentSubjects
        fields = ['student','subjects']
        
class StudentProfileAttributeForm(forms.ModelForm):
    """Form definition for StudentProfile."""
    student = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'student', 'required': 'true'}))
    classteacher = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'classteacher', 'required': 'true'}))
    session = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'session', 'required': 'true'}))
    year = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'year', 'required': 'true'}))
    
    class Meta:
        """Meta definition for StudentProfileform."""

        model = StudentProfileAttribute
        fields = ['student','classteacher','session','year']
