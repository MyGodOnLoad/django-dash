"""analyze URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^dashboard/', include('dash.urls')),
    # django-dash RSS contrib plugin URLs:
    re_path(r'^dash/contrib/plugins/rss-feed/',
            include('dash.contrib.plugins.rss_feed.urls')),

    # django-dash News contrib plugin URLs:
    # re_path(r'^news/', include('news.urls')),

    # django-dash public dashboards contrib app:
    re_path(r'^dash/public/',
            include('dash.contrib.apps.public_dashboard.urls')),
]
