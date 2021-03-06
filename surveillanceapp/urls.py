from django.urls import path, include
from . import views

app_name = 'surveillanceapp'

urlpatterns=[
    path('', views.index, name='index'),
    path('stations/', views.list_stations, name='stationlist'),
    path('stations/<int:pk>', views.station_detail, name='stationdetails'),
    path('stations/<int:station_id>/videos/<int:video_id>', views.surveillance_video, name='video'),
    path('stations/addnewstation/', views.addNewStation, name='stationcreate'),
    path('stations/<int:station_id>/analysis/<int:video_id>', views.surveillance_report, name='report'),
    path('analytics/',views.analytics, name='analytics'),
    path('analytics/filter',views.filter_analytics, name='filter_analytics')
]
