from django.shortcuts import render


def test(request):
    return render(request, "add_question.html", {})

# Create your views here.
