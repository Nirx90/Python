from django import forms

class StudentForm(forms.Form):
    rollno=forms.IntegerField()
    name=forms.CharField()
    dob=forms.DateField()
    marks=forms.IntegerField()
    email=forms.EmailField()
    phonenumber=forms.IntegerField()
    # add=forms.Textarea()
    
