from django.urls import path
from . import views

app_name = 'boot_admin'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),

    path('event.html', views.event, name='event'),
    path('blog.html', views.blog, name='blog'),
    path('user.html', views.user, name='user'),
    path('userEdit.html', views.userEdit, name='userEdit'),
    path('userLogin.html', views.userLogin, name='userLogin'),
    path('userLogout.html', views.userLogout, name='userLogout'),
]
