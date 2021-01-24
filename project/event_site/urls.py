from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='events_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:title>/', views.event_detail ,name='event_detail'),
    path('<int:event_id>/', views.participate ,name='participate')
]
