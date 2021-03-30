from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        "message": "This is not cohort five"
    }
    return render(request, "index.html", context)


def home(request):
    context = {
        "message": "This is cohort five"
    }
    return render(request, "index.html", context)