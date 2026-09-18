from django.urls import path
from .import views

urlpatterns = [
    path('restration/', views.restration, name="restration"),
    path('bussiness_set/', views.bussiness_set, name="bussiness_set"),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.user_login, name="user_login"),
    path('purchase/', views.purchase, name="purchase"),
    path('purchase_list/',views.purchase_list,name="purchase_list"),
    path('update_purchase/<int:id>/',views.purchase,name='update_purchase'),
    path('delete_purchase<int:id>/',views.delete_purchase,name="delete_purchase"),
    path('filter_purchase_data/',views.filter_purchase_data,name="filter_purchase_data")
   

]