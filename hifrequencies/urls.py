"""hifrequencies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainview.views import mainView
from intropage.views import intro
from soundcloud_songs.views import buttonClicked
from news.views import showEntry, lessEntries

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/$', mainView),
    url(r'^$', intro),
    url(r'^ajax/random-song/[0-9]?[0-9]$', buttonClicked),
    url(r'^ajax/load-news/$', showEntry),
    url(r'^ajax/less-news/$', lessEntries)
]

handler404 = 'mainview.views.custom404'
