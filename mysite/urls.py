"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from blog.sitemaps import PostSitemap
from . import views

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('',
         views.home_view, name='home'),
    path('dashboard/',
         views.dashboard,
         name='dashboard'),
#    path('login/',
#         views.user_login,
#         name='login'),
    path('login/',
         auth_views.LoginView.as_view(),
         name='login'),
    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uid64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('time/',
         views.current_datetime), #*** example
    path('time/plus/<int:offset>/',
         views.hours_ahead,
         name='hours_ahead'), # *** example
    path('show_meta/',
         views.show_meta),#*** tools
    path('show_ip/',
         views.show_ip),    #*** tools
    path('resume/',
         include('resume.urls',
                 namespace='resume')),
    path('contact/',
         include('contactApp.urls',
                namespace='contact')),
    path('admin/',
         admin.site.urls),
    path('blog/',
         include('blog.urls',
                 namespace='blog')),
    path('sitemap.xml',
         sitemap,
         {'sitemaps':sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('images/',
         include('images.urls',
                 namespace='images')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
