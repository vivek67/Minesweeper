from django.conf.urls import url

from . import views
app_name = "ms"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createGame/', views.createGame, name='createGame'),
    url(r'^game/(?P<gameId>[0-9]+)/$', views.game, name="game"),
    url(r'^game/(?P<gameId>[0-9]+)/(?P<row>[0-9]+)/(?P<col>[0-9]+)', views.gameAction, name="gameAction"),
]
