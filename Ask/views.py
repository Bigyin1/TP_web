from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def paginator(request, query):
    paginator = Paginator(query, 3)
    page = request.GET.get('page')
    question_list = paginator.get_page(page)
    return question_list


def feed(request):
    questions = []
    for i in range(1, 50):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    return render(request, "feed.html", {'questions': paginator(request, questions)})


def hot(request):
    questions = []
    for i in range(1, 20):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    return render(request, "feed.html", {'questions': paginator(request, questions)})


def ask(request):
    return render(request, "ask.html", {})


def login(request):
    return render(request, "login.html", {})


def question(request, id):
    comments = []
    for i in range(1, 5):
        comments.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    return render(request, "question.html", {'comments': comments})


def signup(request):
    return render(request, "signup.html", {})


def profile(request):
    return render(request, "user_profile.html", {})


def tag(request, tag_name):
    questions = []
    for i in range(1, 30):
        questions.append({
            'title': 'title' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    return render(request, "tag_questions.html", {'questions': paginator(request, questions)})
# Create your views here.
