from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет")

def test(reguest):
    return HttpResponse(' Вторая страница')