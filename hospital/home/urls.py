from django.urls import path,include
from.import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
  
    path('home/',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.department,name='department'),
    path('signup/',views.signup,name='signup'),
    path('',views.login_view,name='login'),
    path('logout/', views.LogoutView, name='logout'),


]