from django.http import HttpResponse

def home(request):
    return HttpResponse('hello this is the home page')