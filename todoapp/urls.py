from django.contrib import admin
from django.urls import path ,include
from todoapp import views

urlpatterns = [
   
    # path('', include('todoapp.urls'))
    path('/create',views.create_todo,name="create_todo"),
    path('/complete/<int:todo_id>',views.complete_todo,name="complete_todo"),
    path('/delete/<int:todo_id>',views.delete_todo,name="delete_todo"),
    path('',views.todo_list,name="Todo_list")
   
]