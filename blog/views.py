from .models import Post
from .serializers import PostSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsAuthorOrReadOnly)
    parser_classes = (MultiPartParser, FormParser)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """
    list and detail actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)
            print('Check permissions')

        return super(UserViewSet, self).get_permissions()
