from django.urls import path
from . import views

app_name = 'dsschool'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),

    # path('qna.html', views.qna, name='qna'),
    # path('board.html', views.board, name='board'),
    # path('boardEdit.html', views.boardEdit, name='boardEdit'),
    # path('boardWrite.html', views.boardWrite, name='boardWrite'),
    # path('boardView.html', views.boardView, name='boardView'),

    # path('userJoin.html', views.userJoin, name='userJoin'),
    # path('userEdit.html', views.userEdit, name='userEdit'),
    # path('userLogin.html', views.userLogin, name='userLogin'),
    # path('userLogout.html', views.userLogout, name='userLogout'),
]
