from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.hello_world),
    path('page/', views.all_pages),
    path('page/<int:pk>', views.page_details)

]


