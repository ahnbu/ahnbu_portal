from django.shortcuts import render
#from app_admin import settings
from .models import Event


def index(request):
    return render(request, 'boot_admin/index.html', {})


def blog(request):
    return render(request, 'boot_admin/blog.html', {})


def user(request):
    return render(request, 'boot_admin/user.html', {})


# def event(request):
#     return render(request, 'boot_admin/event.html', {})


def event(request):
    event_list = Event.objects.all()  # .order_by('-update_date')
    return render(request, 'boot_admin/event.html', {'event_list': event_list})


def userEdit(request):
    return render(request, 'boot_admin/userEdit.html', {})


def userLogin(request):
    return render(request, 'boot_admin/userLogin.html', {})


def userLogout(request):
    return render(request, 'boot_admin/userLogout.html', {})
