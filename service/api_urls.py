from django.urls import path
from .api_view import add_purchase,purchase_list_api,delete_purchase_api,filter_purchase_api
urlpatterns = [
  
   path('add_purchase/',add_purchase.as_view()),
   path('purchase_list_api/',purchase_list_api.as_view()),
   path('edit_purchase/<int:id>/',add_purchase.as_view()),
   path('delete_purchase_api/<int:id>/',delete_purchase_api.as_view()),
   path('filter_purchase_api/',filter_purchase_api.as_view())


]