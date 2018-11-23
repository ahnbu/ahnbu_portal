from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, re_path, include
from django.conf import settings

from index import views
from index.views import HomePageView

urlpatterns = [
    path('', views.index, name='index'),
    path('', HomePageView.as_view(), name='home'),
    # 홈으로 가기 버튼 구현

    path('boot_admin/', include('boot_admin.urls')),
    path('index/', views.index, name='index'),
    path('dsschool/', include('dsschool.urls')),
    path('boot_intro/', include('boot_intro.urls')),
    path('boot_community/', include('boot_community.urls')),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
# static는 debug가 참일 때만 추가하고, false이면 빈값줌

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
