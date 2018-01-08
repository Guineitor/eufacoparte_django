from django.conf.urls import url


from .views import (load_home, load_eventos, load_sobre, load_contato, load_participe ) 


urlpatterns = [
    url(r'^$', load_home, name="index"),
    url(r'^eventos/$', load_eventos, name="eventos"),
    url(r'^sobre/$', load_sobre, name="sobre"),
    url(r'^ajuda/$', load_participe, name="participe"),
    url(r'^contato/$', load_contato, name="contato"),

]