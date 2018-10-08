from django.shortcuts import render


def test(request):
    return render(request, "feed.html", {})

# Create your views here.
