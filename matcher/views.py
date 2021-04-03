from django.http import HttpResponse


def index(request):
    return HttpResponse("matcher app main page")
