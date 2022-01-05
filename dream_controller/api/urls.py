# this is storing all the urls local to this app
from django.urls import path
from .views import RoomView, JournalView, CommentView

urlpatterns = [
    path('home', RoomView.as_view()),
    path('journal', JournalView.as_view()),
    path('comment', CommentView.as_view()),
]
