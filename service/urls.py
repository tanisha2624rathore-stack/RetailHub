from django.urls import path
from .import views

urlpatterns = [
    path('restration/',views.restration,name="restration"),
    path('bussiness_set/',views.bussiness_set,name="bussiness_set"),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('login/',views.login,name="login"),
   

]