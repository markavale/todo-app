from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


#function based get post
@api_view(['GET', 'POST', ])
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    if request.method == "GET":
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', ])
def todo_detail(request, id):
    try:
        todo = Todo.objects.get(id=id)
        data = {}
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TodoSerializer(todo, many=False)
        return Response(serializer.data)

    if request.method =="PUT":
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            data['update'] = "update successful"
            return Response(data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    if request.method =="DELETE":
        todo.delete()
        data['delete'] = "delete successful"
        return Response(data)
        
    
class TodoDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'

#CBV get post
class TodoListCreateView(ListCreateAPIView):
    serializer_class =TodoSerializer
    queryset = Todo.objects.all().order_by('-created_at')
    pagination_class = PageNumberPagination


class TodoViewset(ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer



