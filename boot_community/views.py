from django.shortcuts import render
#from app_admin import settings


def index(request):
    return render(request, 'boot_community/index.html', {})


def board(request):
    return render(request, 'boot_community/board.html', {})


def boardEdit(request):
    return render(request, 'boot_community/boardEdit.html', {})


def boardView(request):
    return render(request, 'boot_community/boardView.html', {})


def boardWrite(request):
    return render(request, 'boot_community/boardWrite.html', {})


def qna(request):
    return render(request, 'boot_community/qna.html', {})


def userJoin(request):
    return render(request, 'boot_community/userJoin.html', {})


def userEdit(request):
    return render(request, 'boot_community/userEdit.html', {})


def userLogin(request):
    return render(request, 'boot_community/userLogin.html', {})


def userLogout(request):
    return render(request, 'boot_community/userLogout.html', {})
