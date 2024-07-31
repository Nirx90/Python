from django.shortcuts import render,redirect
from app.models import Student
# Create your views here.
def home(request):
    data = Student.objects.all()
    contaxt = {
        'data':data
    }
    return render(request,'app/index.html',contaxt)

def about(request):
    return render(request,'app/about.html')

def insertData(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Student(name=name,email=email,age=age,gender=gender)
        query.save()
    return redirect('home')

def updateData(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender

        edit.save()
        return redirect('home')
    
    data = Student.objects.get(id=id)
    context = {"data":data}
    return render(request,'app/update.html',context)

def deleteData(request,id):
    de = Student.objects.get(id=id)
    de.delete()
    return redirect('home')
