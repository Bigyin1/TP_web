from django.urls import path
from Ask.views import *

urlpatterns = [
    path('', feed, name='main'),
    path('hot', feed, name='hot'),
    path('ask', ask, name='ask'),
    path('question/<int:id>', question, name='question'),
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path('profile', profile, name='profile'),
    path('tag/<str:tag_name>', tag, name='tag'),
]