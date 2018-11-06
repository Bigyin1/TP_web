from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import *


def paginator(request, query):
    paginator = Paginator(query, 3)
    page = request.GET.get('page')
    question_list = paginator.get_page(page)
    return question_list


class FeedView(ListView):
    paginate_by = 3
    model = Question
    ordering = "date"
    template_name = "feed.html"


class QuestionView(DetailView):
    model = Question
    template_name = "question.html"


class HotQuestionsView(ListView):
    paginate_by = 3
    model = Question
    ordering = "rate"
    template_name = "feed.html"


class TagQuestionView(ListView):
    paginate_by = 3
    template_name = "tag_questions.html"
    context_object_name = "questions"

    def get_context_data(self, **kwargs):
        context = super(TagQuestionView, self).get_context_data(**kwargs)
        context["tag"] = self.kwargs["tag_name"]
        return context

    def get_queryset(self):
        return Tag.objects.questions_by_tag(self.kwargs['tag_name'])


def ask(request):
    return render(request, "ask.html", {})


def login(request):
    return render(request, "login.html", {})


def signup(request):
    return render(request, "signup.html", {})


def profile(request):
    return render(request, "user_profile.html", {})

