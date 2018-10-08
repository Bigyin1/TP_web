from django.urls import path
from Ask.views import test

urlpatterns = [
    path('', test),
]