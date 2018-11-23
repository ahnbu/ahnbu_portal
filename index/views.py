from django.views.generic.base import TemplateView
from django.shortcuts import render
#from boot_admin import settings


def index(request):
    return render(request, 'index/index.html', {})


# from articles.models import Article


class HomePageView(TemplateView):

    template_name = "index.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context


# def blog(request):
#     return render(request, 'boot_admin/blog.html', {})


# def user(request):
#     return render(request, 'boot_admin/user.html', {})


# def event(request):
#     return render(request, 'boot_admin/event.html', {})


# def userEdit(request):
#     return render(request, 'boot_admin/userEdit.html', {})


# def userLogin(request):
#     return render(request, 'boot_admin/userLogin.html', {})


# def userLogout(request):
#     return render(request, 'boot_admin/userLogout.html', {})
