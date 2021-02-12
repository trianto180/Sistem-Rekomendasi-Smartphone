from django.contrib import admin
from django.urls import path
from rekomendasi.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('rekomendasi/', rekomendasi, name='rekomendasi'),
]
