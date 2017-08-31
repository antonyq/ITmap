from django.shortcuts import get_object_or_404, render

# from locale import localize

def tests(request):
    # locale = localize('search', 'ru')
    return render(request, 'polls/detail.html', {'locale': locale})