from django.shortcuts import render
#from app_admin import settings


def index(request):
    return render(request, 'boot_intro/index.html', {})
