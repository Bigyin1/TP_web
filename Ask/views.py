from django.shortcuts import render


def test(request):
    return render(request, "question_details.html", {})

# Create your views here.
