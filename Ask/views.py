from django.shortcuts import render


def test(request):
    return render(request, "signup.html", {})

# Create your views here.
