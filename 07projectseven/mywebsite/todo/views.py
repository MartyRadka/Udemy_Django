from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.views.decorators.http import require_POST

def index(request):
    """basicle loading of the database"""
    mytodo = Todo.objects.order_by('id')
    form = TodoForm
    context = {
        'mytodo': mytodo,
        'form': form
    }
    return render(request, 'todo/index.html', context)


"""what happen when someone click on it"""
@require_POST
def addNewTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():  # if the are the completes data in Form
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')


def completeTodo(request, todo_id):
    mytodo = Todo.objects.get(pk=todo_id)
    mytodo.complete = True  # .complete comes from models!
    mytodo.save()  # don't forget to save it

    return redirect('index')


def deleteTodo(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')
