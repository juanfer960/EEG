from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('logup/',views.logup,name='logup'),
    path('singout/',views.singout,name='singout'),
    path('search/<user>-<password>/',views.search,name='search'),
    path('home/<user>-<password>/',views.home,name='home'),
    path('fileSerch/<user>-<password>/',views.fileSerch,name='fileSerch'),
    path('eegSerch/<user>-<password>/',views.eegSerch,name='eegSerch'),
    path('plot/<user>-<password>/',views.plot,name='plot'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 