from django.contrib import admin
from django.urls import path
from rekomendasi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smartphone', smartphone, name='smartphone'),
    path('rekomendasi/', res, name='res'),
]