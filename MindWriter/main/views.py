from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html', {'title': 'MindWriter'})


def about(request):
    return HttpResponse("About", {'title': 'About'})
