from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('getResources/', views.getResources, name='resources'),
    path('resourceDetails/<int:id>', views.resourceDetails, name='resourcedetails'),
    path('getMeeting/', views.getMeeting, name='meeting'),
    path('meetingDetails/<int:id>', views.meetingDetails, name='meetingdetails'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]