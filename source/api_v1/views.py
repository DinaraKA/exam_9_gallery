from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_v1.serializer import CommentSerializer, LikeSerializer
from webapp.models import Comment, Like


class CommentViewSet(ModelViewSet):
    # permission_classes = IsAuthenticated
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer