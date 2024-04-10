from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
def todo(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TaskForm()
    
    tasks = Task.objects.all()
    
    return render(request, 'index.html', {'form': form, 'tasks': tasks})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return JsonResponse({'message': 'Task deleted successfully'})