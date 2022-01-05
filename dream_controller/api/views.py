from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, JournalSerializer, CommentSerializer
from .models import Room, Journal, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
# this is where our endpoints go which is the location on the webserver

# a view that is set up to return all the rooms


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# class CreateUserView(APIView):
#     serializer_class = CreateUserSerializer

#     def post(self, request, format=None):
#         pass


# class UserView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class CreateJournalView(APIView):
#     serializer_class = CreateJournalSerializer

#     def post(self, request, format=None):
#         pass


class JournalView(generics.CreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class CommentView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
