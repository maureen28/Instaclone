"""gram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth import views
from ig.views import welcome, search_results, get_comments, messages

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', welcome, name = 'welcome'),
    url(r'messages/', messages, name='messages'),
    url(r'comments/', get_comments, name='get_comments'),
    url(r'search/', search_results, name='search_results'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$',views.logout, {"next_page": '/'}),
]

