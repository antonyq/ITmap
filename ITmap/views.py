from django.shortcuts import get_object_or_404, render

from .locale import localize

def header(request):
    locale = localize('header', 'ru')
    return render(request, 'polls/detail.html', {'locale': locale})

def footer(request):
    locale = localize('footer', 'ua')
    return render(request, 'polls/detail.html', {'locale': locale})