from django.urls import path
from django.views.generic import TemplateView
from contactApp import views
from mysite import views as mysite_views

app_name = 'contactApp'

urlpatterns = [
    #post views
#    path('', views.PostListView.as_view(), name='post_list'),
    path('', views.contact,
         name='contact'),
    path('thanks/',
         TemplateView.as_view(template_name='email_thanks.html')),
]
