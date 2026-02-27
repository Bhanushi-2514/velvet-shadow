from django.urls import path
from shadowverse import views

urlpatterns = [
    path('', views.index, name="index"),
    path('story/<str:trope>/', views.story_page, name="story"),
    path('shadow-chamber/', views.shadow_chamber, name="shadow_chamber"),
]
