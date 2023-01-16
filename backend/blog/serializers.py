from rest_framework import serializers
from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('id', 'title', 'thumbnail', 'slug', 'excerpt', 'content', 'published', 'author', 'status')