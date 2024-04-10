from django.urls import path
from .views import todo, delete_task  

urlpatterns = [
    path('', todo, name='todo'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'), 
]
