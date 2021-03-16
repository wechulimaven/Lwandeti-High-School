from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from . forms import LibraryAssetForm
from subjects.models import Subject
# from Department.models import Departments
from . models import LibraryAsset
# Create your views here.
def add_asset(request):
    context = {}
    subject_qs = Subject.objects.all()
    # dept_qs = Departments.objects.all()
    context['subject_qs'] = subject_qs
    # context['dept_qs'] = dept_qs
    if request.method == 'POST':
        lib_form = LibraryAssetForm(request.POST)
        if lib_form.is_valid():
            title = request.POST['title'],
            obj = lib_form.save(commit = False)
            # obj.department = request.POST['department']
            obj.asset_type = request.POST['asset_type']
            obj.save()
            messages.success(request, f'{title} Created Successfully !')
            return redirect('staff:all_asset')
        else:
            messages.success(request, f'Some Fields Are Missing!')
            return redirect('staff:add_asset')
    else:
        lib_form = LibraryAssetForm()
        context['lib_form'] = lib_form

    return render(request, 'library/add_asset.html', context)

def all_asset(request):
    context = {}
    asset_qs = LibraryAsset.objects.all()
    context['asset_qs'] = asset_qs
    return render(request, 'library/all_asset.html', context)

def edit_asset(request, id):
    context