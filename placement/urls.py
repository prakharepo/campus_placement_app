from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^index/$',views.index, name='index'),
    url(r'^show_company/$',views.show_company, name='show_company'),
    url(r'^announcement/$',views.announcement, name='announcement'),
    path('show_description/<int:company_id>',views.show_description,name='show_description'),
    url(r'^show_campus/$',views.show_campus, name='show_campus'),
]