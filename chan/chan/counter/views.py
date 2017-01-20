from django.shortcuts import render


def counter_view(request):
    return render(request, 'counter/counter_view.html')
