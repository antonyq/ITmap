from django.shortcuts import get_object_or_404, render

from ITmap.locale import localize

def index(request):
    locale = localize('header', 'ru')
    # print('OUTPUT')
    # for key, value in locale['paragraphs'].items():
    #     print(key, value, '/n')
    # print('OUTPUT')
    return render(request, 'index.html', {
        'locale': locale['paragraphs'], 
        'language': 'ru', 
        'sitename': 'ITmap', 
    })