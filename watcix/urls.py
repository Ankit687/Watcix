from django.urls import path

from . import views
from .views import signup

urlpatterns = [
    path('', views.watcixHome),
    path('watcix/', views.watcixHome),
    path('home/', views.home),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('movie/', views.movie),
    path('webSeries/', views.webSeries)
]
