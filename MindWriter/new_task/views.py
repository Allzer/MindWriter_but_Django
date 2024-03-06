from django.http import HttpResponse
from django.shortcuts import render

def get_tasks(request):
    return render(request, 'main/tasks.html',{'title':'Tasks'})