from django import forms
from . models import LibraryAsset


class LibraryAssetForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'title', 'required': 'true'}))
    author_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'author_name', 'required': 'true'}))
    purchase_date = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'date', 'required': 'true'}))
    publisher = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'publisher', 'required': 'true'}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'list2', 'tabIndex':'-1', 'required': 'true'}))
    department = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'list5', 'tabIndex':'-1', 'required': 'true'}))
    asset_type = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'asset_type', 'required': 'true'}))
    status = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'status',  'required': 'true'}))
    price = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'mdl-textfield__input', 'id': 'price',  'required': 'true'}))
    asset_details = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'mdl-textfield__input', 'id': 'asset_details', 'rows': '4', 'required': 'true'}))
    class Meta:
        model = LibraryAsset
        fields = ['title','author_name','status','purchase_date','publisher','department','subject','price','asset_type', 'asset_details']