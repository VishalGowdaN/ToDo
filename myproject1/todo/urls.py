from django.urls import path
from .views import *

urlpatterns=[
    path('todos/',ToDoListView.as_view(),name='todo-list'),
    path('todos/create/',ToDoCreateView.as_view(),name='todo-create'),
    path('todos/<int:pk>',ToDoDetailView.as_view(),name='todo-detail'),
    path('todos/<int:pk>/update/',ToDoUpdateView.as_view(),name='todo-update'),
    path('todos/<int:pk>delete/',ToDoDeleteView.as_view(),name='todo-delete'),       
]
