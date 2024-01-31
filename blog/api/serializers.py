from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post,comments, Category

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','title','body','owner','comment','categories']

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']

class UserSerializer(serializers.ModelSerializer):
    #many to one relationship
    # if read_only = true is not set it will have write access by default
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model  = User
        fields = ['id','username','posts','comment', 'categories']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    
    class Meta:
        model = comments
        fields = ['id','body','owner','post']