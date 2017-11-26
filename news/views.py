from django.shortcuts import get_object_or_404, render, render_to_response

from ITmap.locale import localize

def news(request):
    return render_to_response('news.html', {
        'posts': Article.objects.all()[:5]
    })
    
    # language = language or 'ru'
    # locale_header, locale_news, locale_footer = localize(language, ['header', 'news', 'footer'])
    # return render(request, 'index.html', {
    #     'locale': {
    #         'meta': locale_index['meta'],
    #         'language': language,
    #         'header': locale_header,
    #         'main': locale_news,
    #         'footer': ''
    #     },
    #     'sitename': 'ITmap'
    # })

def article(request):
    return render_to_response('article.html', {
        'posts': Article.objects.filter()
    })