from django.urls import path
from .views import todo_list, TodoListCreateView, todo_detail, TodoDetailView, TodoViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TodoViewset)


app_name="todo"

urlpatterns = [
    #function based
   path('todo-list/', todo_list, name="list"),
   path('todo-list/<id>/', todo_detail, name="detail"),


   # Class based view
   path('todos/', TodoListCreateView.as_view(), name="lists"),
   path('todos/<id>/', TodoDetailView.as_view(), name="detail-todo")
]

urlpatterns += router.urls
