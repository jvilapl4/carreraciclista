from django.http import HttpResponse


def index(request):
    return HttpResponse("Tour de Francia 2024")