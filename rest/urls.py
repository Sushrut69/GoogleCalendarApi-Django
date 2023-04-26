from django.contrib import admin
from django.urls import path
from rest import views


urlpatterns = [
    path('home',views.index, name = 'home' ),
    path('v1/calendar/init' , views.GoogleCalendarInitView, name='google_permisssion'),
    path('v1/calendar/redirect', views.GoogleCalendarRedirectView, name='google_redirect')
]