from django.conf.urls import url, include
from django.contrib import admin
from minesweeper.views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^minesweeper/', include('minesweeper.urls')),
]
