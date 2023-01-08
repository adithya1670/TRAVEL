

from.import views
from django.urls import path

urlpatterns = [
    path('login',views.login,name='login'),
    # path ('',views.demo,name='demo'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout')
]