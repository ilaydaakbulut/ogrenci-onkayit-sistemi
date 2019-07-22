from django.conf.urls import url
from django.urls import include, path

from .views import ogrenci_kayit,ogrenci_viewt
app_name = "ogrenci"
urlpatterns= [
    path('ogrenci_kayit/', ogrenci_kayit, name='ogrenci_kayit'),
    path('ogrenci_kayit/<int:id>/', ogrenci_viewt, name='ogrenci_kayit_id'),
]