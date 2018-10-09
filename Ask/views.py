from django.shortcuts import render


def test(request):
    return render(request, "question.html", {})

# Create your views here.
