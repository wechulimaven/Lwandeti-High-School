from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from teachers.models import TeacherProfile
from staff.models import TeachersProfileAttrib, StudentProfileAttribute, StudentSubjects

class TeachersProfileForm(forms.ModelForm):
    """Form definition for StudentProfile."""
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'first_name', 'required': 'true'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'last_name', 'required': 'true'}))
    id_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'id_number', 'required': 'true'}))

    class Meta:
        """Meta definition for StudentProfileform."""

        model = TeacherProfile
        fields = ['first_name','last_name','id_number']
        
class TeachersProfileAttribForm(forms.ModelForm):
    """Form definition for StudentProfile."""
    mobile_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'mobile_number', 'required': 'true'}))
    designation = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'designation','tabIndex': '-1', 'readonly': 'true', 'required': 'true'}))
    gender = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'gender','tabIndex': '-1', 
               'readonly': 'true', 'required': 'true'}))
    dob = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'dateOfBirth',  'required': 'true'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'address', 'required': 'true'}))
    educational_status = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'educational_status', 'required': 'true'}))
    joined_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'joined_date', 'required': 'true'}))
    profile_photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone','id': 'profile_photo', 'accept':'image/*', 'required': 'true'}))
       
    class Meta:
        """Meta definition for TeachersProfileform."""

        model = TeachersProfileAttrib
        fields = ['mobile_number','designation','gender','dob','address','educational_status','joined_date','profile_photo']

class StudentProfileAttributeForm(forms.ModelForm):
    class Meta:
        model = StudentProfileAttribute
        fields = ['student', 'classteacher', 'formclass', 'session', 'year']

class StudentSubjectsForm(forms.ModelForm):
    class Meta:
        model = StudentSubjects
        fields = ['classteacher', 'student', 'subjects']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_email', 'placeholder': 'Email programme', 'required': 'true'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password1','placeholder':'Password', 'required': 'true'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password2','placeholder':'Confirm Password', 'required': 'true'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input100', 'id': 'id_username', 'placeholder':'Username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'input100', 'id': 'id_password', 'placeholder':'Password','required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(UserLoginForm, self).clean(*args, **kwargs)