from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def todo_list(request):
    todos =Todo.objects.order_by('-id')
    return render(request, 'index.html',{'todos':todos})

def create_todo(request):
    if request.method == 'POST':
        title= request.POST.get("title")
        description=request.POST.get('description')
        # todo_date= request.Post.get('todo_date')
        # progress = int(request.POST.get('progress', 0))
        Todo.objects.create(title=title, description=description )      
    return redirect('Todo_list')

def complete_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.completed=True
    todo.save()
    return redirect('Todo_list')

def delete_todo(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('Todo_list')