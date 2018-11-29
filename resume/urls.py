from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'resume'

urlpatterns = [
    #post views
#    path('', views.PostListView.as_view(), name='post_list'),
    path('',
         views.front_page,
         name='front_page'),
    #path('download_pdf/',
    #     views.download_pdf,
    #     name='download_pdf'),

]
