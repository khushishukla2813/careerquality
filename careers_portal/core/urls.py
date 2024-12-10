from django.urls import path
from . import views

urlpatterns = [
    path('Register/', views.Register, name='signup'),  # Name for the home page URL
    # Other URL patterns
     
    # Other URL patterns
    path('login/', views.login_view, name='login'),
     path('', views.index, name='index'),
      path('partnership/', views.partnership_view, name='partnership'),  # Redirects to partnership page
    path('candidate/', views.candidate_view, name='candidate'),  

]
