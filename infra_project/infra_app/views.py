from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось исправить проблему с ssh!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
