from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from gram.views import welcome, search_results, comments, messages, image_form,explore

urlpatterns = [
    url(r'messages/', messages, name='messages'),
    url(r'explore/', explore, name='explore'),
    url(r'search/', search_results, name='search_results'),
    url(r'comments/',comments, name='comments'),
    url(r'^admin/', admin.site.urls),
    url('', welcome, name = 'welcome'),
    url(r'profile/', image_form, name='image_form'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$',views.logout, {"next_page": '/'}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)