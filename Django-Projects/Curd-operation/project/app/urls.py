from django.urls import path
from app import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('about/',views.about , name='about' ),
    path('insertData/',views.insertData,name='insertData' ),
    path('update/<id>/',views.updateData,name='updateData' ),
    path('delete/<id>/',views.deleteData,name='deleteData'),
]