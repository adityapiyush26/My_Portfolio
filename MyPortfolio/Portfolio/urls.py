from django.urls import path
from Portfolio import views

app_name = 'Portfolio'

urlpatterns = [
    path('', views.home, name="home"),
    path('', views.resume, name="resume"),
    path('', views.projects, name="projects"),
    path('', views.contact, name="contact"),
    path('', views.users, name="Users"),
]
