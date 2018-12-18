from django.urls import path
from Ask.views import *

urlpatterns = [
    path('', FeedView.as_view(), name='main'),
    path('hot', HotQuestionsView.as_view(), name='hot'),
    path('ask', AskView.as_view(), name='ask'),
    path('question/<pk>', QuestionView.as_view(), name='question'),
    path('login', LogInView.as_view(), name="login"),
    path('signup', SignUpView.as_view(), name="signup"),
    path('signout', sign_out, name='signout'),
    path('profile', profile, name='profile'),
    path('tag/<str:tag_name>', TagQuestionView.as_view(), name='tag'),
]