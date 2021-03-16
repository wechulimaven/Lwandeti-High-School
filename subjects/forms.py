from django import forms
from . models import Subject, SubjectSyllabus, SubjectObjective


class SubjectForm(forms.ModelForm):
    # formclass = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'mdl-textfield__input', 'id': 'subject_class', 'required': 'true'}))
    subject_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_name', 'required': 'true'}))
    subject_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'subject_code', 'required': 'true'}))
    subject_photo = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'dropzone','id': 'subject_photo', 'accept':'image/*', 'required': 'true'}))
    class Meta:
        model = Subject
        fields = ['formclass','subject_name','subject_code','subject_photo']
    
class SubjectSyllabusForm(forms.ModelForm):

    syllabus = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'syllabus', 'rows': '3', 'required': 'true'}))

    class Meta:
        model = SubjectSyllabus
        fields = ['subject','syllabus']

class SubjectObjectiveForm(forms.ModelForm):
    
    objective = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'objective', 'rows': '4', 'required': 'true'}))

    class Meta:
        model = SubjectObjective
        fields = ['subject','objective']