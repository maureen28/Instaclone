from django.conf.urls import url
from . import views
from django.conf.urls.static import static
# from django.conf import settings

urlpatterns=[
    url(r'^welcome/$',views.welcome,name='index'),
    url(r'^$', views.home, name = 'welcome'),
    url(r'^new/post/$', views.post, name = 'post'),
    url(r'^image_form/$', views.image_form, name='image_form'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)