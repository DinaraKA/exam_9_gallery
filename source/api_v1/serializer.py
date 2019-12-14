from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from webapp.models import Comment, Like


class CommentSerializer(ModelSerializer):
    comment_author = serializers.CharField(read_only=True)
    comment_created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Comment
        fields = ['id', 'text', 'comment_author', 'comment_created_at']


class LikeSerializer(ModelSerializer):
    user = serializers.CharField(read_only=True)
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'photo']

