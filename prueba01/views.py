from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hola mundo, primer ejercicio")