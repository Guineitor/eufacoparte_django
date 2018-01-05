from django.conf.urls import url


from .views import (home) 


urlpatterns = [
    url(r'^$', load_home, name="index"),
    url(r'/eventos/^$', BuildPage.as_view(), name="eventos"),
    url(r'^/sobre/$', BuildPage.as_view(), name="sobre"),
    url(r'^/ajuda/$', BuildPage.as_view(), name="participe"),
    url(r'^/contato/$', BuildPage.as_view(), name="contato"),

]