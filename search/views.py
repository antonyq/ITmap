from django.shortcuts import get_object_or_404, render

from ITmap.locale import localize

def search(request, language):
    language = language or 'ru'
    locale_header, locale_index, locale_footer = localize(language, ['header', 'index', 'footer'])
    return render(request, 'search.html', {
        'locale': {
            'meta': locale_index['meta'],
            'language': language,
            'header': locale_header,
            'main': '',
            'footer': ''
        },
        'sitename': 'ITmap'
    })