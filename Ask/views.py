from django.shortcuts import render


def test(request):
    return render(request, "login_form.html", {})

# Create your views here.
