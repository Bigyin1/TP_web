from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


class FeedView(ListView):
    paginate_by = 3
    model = Question
    ordering = ["-date"]
    template_name = "feed.html"


class QuestionView(DetailView):
    model = Question
    template_name = "question.html"
    form_class = AnswerForm

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        print(self.object)
        form = self.form_class(request.POST)
        if form.is_valid():
            answer = Answer.objects.create(author=request.user,
                                           text=form.cleaned_data['text'],
                                           question=self.object)
            answer.save()
            return self.render_to_response(context)
        else:
            context['form'] = form
            return self.render_to_response(context)


class HotQuestionsView(ListView):
    paginate_by = 3
    model = Question

    ordering = ["-rate"]
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


class AskView(LoginRequiredMixin, FormView):
    form_class = NewQuestionForm
    template_name = 'ask.html'
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            question = Question.objects.create(author=request.user,
                                               title=form.cleaned_data['title'],
                                               text=form.cleaned_data['text'])
            question.save()
            form.cleaned_data['tags'].strip()
            print(form.cleaned_data['tags'])
            for tagTitle in form.cleaned_data['tags'].split():
                tag = Tag.objects.get_or_create(title=tagTitle)[0]
                question.tags.add(tag)
                question.save()
            return HttpResponseRedirect(reverse('question', args=[question.pk]))
        else:
            return self.form_invalid(form)


@login_required(login_url='login')
def sign_out(request):
    logout(request)
    return redirect('/')


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = "signup.html"
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return redirect(self.success_url)


class LogInView(FormView):
    form_class = SignInForm
    template_name = "login.html"
    success_url = '/'

    def form_valid(self, form):
        print(self.get_form_kwargs())
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        login(self.request, user)
        return redirect(self.success_url)


def profile(request):
    return render(request, "user_profile.html", {})

