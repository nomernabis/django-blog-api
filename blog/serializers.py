from rest_framework import serializers
from blog.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    text_preview = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', 'created', 'text_preview', 'image')
        
    def get_text_preview(self, obj):
        return obj.text[:120]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'posts')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
