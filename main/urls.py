from django.urls import path,include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('init', views.init),
    path('create', views.create, name='create'),
    path('', include('social_django.urls')),
    # path(r'^register/$', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('register', RegisterUser.as_view(), name='register')
]
