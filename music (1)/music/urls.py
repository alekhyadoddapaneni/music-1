"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


from app import views
from music import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.MusicHome.as_view(),name="musichome"),
    path("upload/",views.UploadSongs.as_view(),name="upload"),
    path("viewsongs/",views.Viewsongs.as_view(),name="viewsongs"),
    path("deletesongs/",views.DeleteSongs.as_view(),name="deletesongs"),
    path("search/",views.SearchSong.as_view(),name="search"),
    path('playsong/',views.PlaySong.as_view(),name="playsong")
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)