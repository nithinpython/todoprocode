from django.shortcuts import render, redirect

# Create your views here.
from todoapp.forms import todoform
from todoapp.models import Task


def demo(request):
    new = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get("task", '')
        priority = request.POST.get("priority", '')
        date= request.POST.get("date",'')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, "index.html", {'data': new})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    s = todoform(request.POST or None, instance=task)
    if s.is_valid():
        s.save()
        return redirect('/')
    return render(request, 'update.html', {'f': s, 'task': task})
