from rest_framework import serializers
from . models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('__all__')
        extra_kwargs = {
            'read_only':'created_at',
        }
        
