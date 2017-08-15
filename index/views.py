from django.shortcuts import get_object_or_404, render

from ITmap.locale import localize

def index(request):
    locale = localize('header', 'ru')
    print(locale['paragraphs'])
    return render(request, 'index.html', {
        'locale': locale, 
        'language': 'ru', 
        'sitename': 'ITmap', 
    })