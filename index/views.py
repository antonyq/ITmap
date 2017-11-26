from django.shortcuts import get_object_or_404, render

from ITmap.locale import localize


def index(request, language):
    language = language or 'ru'
    locale_header, locale_index, locale_footer = localize(language, ['header', 'index', 'footer'])
    return render(request, 'index.html', {
        'locale': {
            'meta': locale_index['meta'],
            'language': language,
            'header': locale_header,
            'main': locale_index,
            'footer': ''
        },
        'sitename': 'ITmap'
    })