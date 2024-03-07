from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from . import models

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'name', 'password'
        )
        
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogPost
        fields = '__all__'
    #     fields = [
    #     'title', 'slug', 'category', 'thumbnail1', 'thumbnail2',
    #     'thumbnail3', 'thumbnail4', 'thumbnail5',
    #     'excerpt', 'month', 'day', 'content', 'featured', 'date_created'
    # ]
        lookup__field = 'slug'
        
        