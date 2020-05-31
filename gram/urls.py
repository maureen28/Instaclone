from django.conf.urls import url
from gram.views import welcome, search_results, comments, messages,explore, image_form
from django.conf.urls.static import static


urlpatterns=[
    url(r'profile/', image_form, name='image_form'),
    url(r'messages/', messages, name='messages'),
    url(r'explore/', explore, name='explore'),
    url(r'search/', search_results, name='search_results'),
    url(r'comments/',comments, name='comments'),
    url('', welcome, name = 'welcome'),
]