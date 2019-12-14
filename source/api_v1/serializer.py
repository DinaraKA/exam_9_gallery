from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from webapp.models import Comment, Like


class CommentSerializer(ModelSerializer):
    comment_author = serializers.CharField(read_only=True)
    comment_created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")


    def create(self, request):
        user = self.context['request'].user
        photo = request['photo']
        text = request['text']
        comment = Comment.objects.create(comment_author=user, photo=photo, text=text)
        return comment

    class Meta:
        model = Comment
        fields = ['id', 'text', 'photo', 'comment_author', 'comment_created_at']


class LikeSerializer(ModelSerializer):
    user = serializers.CharField(read_only=True)
    photo = serializers.CharField(read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'user', 'photo']

