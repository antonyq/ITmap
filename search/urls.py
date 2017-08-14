from django.shortcuts import get_object_or_404, render

from ../../locale import localize

def search(request):
    # locale = localize('header', 'ru')
    return render(request, 'search.html', {'locale': locale})