from django.urls import path,include
from . import views,admin
urlpatterns = [
    path('',views.login,name='Login'),
    
]