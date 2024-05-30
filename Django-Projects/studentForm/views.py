from django.shortcuts import render

# Create your views here.
# def homepage(request):
#     return render(request,'web1/home.html')

from . import forms

def StudentInputForm(request):
    fm = forms.StudentForm()

    if request.method == 'POST':
        fm = forms.StudentForm(request.POST)
        if fm.is_valid():
            print("succes submited")
            print('rollno: ',fm.cleaned_data['rollno'])
            print('name: ',fm.cleaned_data['name'])
            print('dob: ',fm.cleaned_data['dob'])
            print('marks: ',fm.cleaned_data['marks'])
            print('email: ',fm.cleaned_data['email'])
            print('ph: ',fm.cleaned_data['phonenumber'])
            # print('address: ',fm.cleaned_data['add'])

    return render(request,'web1/home.html',{'empForm':fm})


