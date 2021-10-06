from api import views
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import UserApi,SaveFile

urlpatterns = [
    path('user/',views.UserApi),
    #path('user/([0+9]+)/',views.UserApi),
    path('user/<int:id>/',UserApi),
    path('user/savefile/',SaveFile),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)