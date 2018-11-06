from django.urls import path
from Ask.views import *

urlpatterns = [
    path('', FeedView.as_view(), name='main'),
    path('hot', HotQuestionsView.as_view(), name='hot'),
    path('ask', ask, name='ask'),
    path('question/<pk>', QuestionView.as_view(), name='question'),
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path('profile', profile, name='profile'),
    path('tag/<str:tag_name>', TagQuestionView.as_view(), name='tag'),
]