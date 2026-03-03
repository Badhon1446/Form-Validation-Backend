from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('create/', views.create, name = 'create'),
    path('students/', views.student_list, name='students'),
    path('update/<int:id>/', views.update_student, name='update'),
    path('delete/<int:id>/', views.delet_student, name='delete')
    
]
