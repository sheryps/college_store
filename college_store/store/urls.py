
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('collegestore',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('load_courses',views.load_courses,name='load-courses'),
    path('details',views.details,name='details')
]