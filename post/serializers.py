from rest_framework import serializers
from . import models
from user.models import User as user_model


class FeedAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_model
        fields = (
            "id",
            "username",
            "profile_photo",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = FeedAuthorSerializer()

    class Meta:
        model = models.Comment
        fields = (
            "id",
            "contents",
            "author",  # 코멘트 모델에 있음 / 코멘트 적은 사람 가져오기
        )


class PostSerializer(serializers.ModelSerializer):
    comment_post = CommentSerializer(many=True)
    author = FeedAuthorSerializer()
    create_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = models.Post
        fields = (
            "id",
            "image",
            "caption",
            "comment_post",
            "author",
            "create_at",
            "post_likes",
            "tags",
        )
