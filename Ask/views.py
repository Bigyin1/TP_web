from django.shortcuts import render


def test(request):
    return render(request, "user_profile.html", {})

# Create your views here.
