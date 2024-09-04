from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/<int:pk>/comment/', views.add_comment_to_event, name='add_comment_to_event'),
    path('api/', include('events.api_urls')),
    
]
