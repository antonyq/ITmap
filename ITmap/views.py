from django.http import HttpResponse


def index(request):
    return HttpResponse("index")

def search(request):
    return HttpResponse("search")

def news(request):
    return HttpResponse("news")

def about(request):
    return HttpResponse("about")