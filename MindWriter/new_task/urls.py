from django.urls import path

from new_task import views

urlpatterns = [
    path('', views.get_tasks, name='Tasks')
]