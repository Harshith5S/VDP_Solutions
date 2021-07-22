from django.contrib.staticfiles.urls import static
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from p3 import settings
from . import views

urlpatterns = [
    path('', views.startpage, name='startpage'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('tea', views.tea, name='tea'),
    path('galis', views.galis, name='galis'),
    path('fairandlovely', views.fairandlovely, name='fairandlovely'),
    path('cigarette', views.cigarette, name='cigarette'),
    path('biscuit', views.biscuit, name='biscuit'),
    path('panaka', views.panaka, name='panaka'),
    path('teaform', views.teaform, name='teaform'),
    path('galisform', views.galisform, name='galisform'),
    path('fairandlovelyform', views.fairandlovelyform, name='fairandlovelyform'),
    path('cigaretteform', views.cigaretteform, name='cigaretteform'),
    path('biscuitform', views.biscuitform, name='biscuitform'),
    path('panakaform', views.panakaform, name='panakaform'),
    path('contactform', views.contactform, name='contactform'),
]


urlpatterns += staticfiles_urlpatterns()
