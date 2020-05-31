from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

from gram.views import logout_view, my_view, password_change

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('gram.urls')),
    url('logout/', logout_view, name = 'logout_view'),
    url('login/', my_view, name = 'my_view'),
    url('password/', password_change, name = 'password_change'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)