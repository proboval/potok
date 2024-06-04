from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_user, name='logout'),
]
