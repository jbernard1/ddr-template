from django.shortcuts import render


def index(request):
    return render(request, 'index.html', dict(
        title="You did it!",
    ))
