from django.shortcuts import get_object_or_404, render

from ITmap.locale import localize


def index(request):
    locale = localize('header', 'ru')
    return render(request, 'index.html', {
        'locale': {
            'meta': {
                'title': 'ITmap',
                'description': 'все курсы программирования в Киеве',
                'keywords': [
                    'курсы',
                    'программирование',
                    'Киев',
                    'Харьков',
                    'Львов',
                    'Одесса',
                ],
            },
            'header': locale,
            'main': '',
            'footer': ''
        },
        'language': 'ru', 
        'sitename': 'ITmap'
    })