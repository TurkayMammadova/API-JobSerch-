from django.urls import path
from .views import *

urlpatterns = [
  
    path('vacancies', allVacancies, name = 'vacancies'),
    path('update_likes/', update_likes, name='update_likes'),
    path('update_views_count/', update_views_count, name='update_views_count'),
    
]
