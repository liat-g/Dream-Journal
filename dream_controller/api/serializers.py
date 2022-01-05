from rest_framework import serializers
from .models import Room, Journal, Comment, User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
                  'votes_to_skip', 'created_at')


# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('is_dreamer')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'user_name')


# class CreateJournalSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('user', 'content', 'is_draft', 'journal_rating')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('id', 'created_at', 'content',
                  'is_draft', 'journal_rating')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment_on', 'is_approved')
