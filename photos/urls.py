from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'photos'
urlpatterns = [
    path('add_Comment', views.Add_Comment, name="add_Comment"),
    path('',views.photos_home,name="photos_home"),
    path('my_photos',views.my_photos,name="my_photos"),  
    path('add_photos',views.add_photos,name="add_photos"),
    path('update<int:id>',views.updatephotopost,name="update"),
    path('delete_photos<int:id>',views.delete_photos,name="delete_photos"),
    path('deletecomment<int:id>',views.deletecomment,name="deletecomment"),
    path('like',views.postlike,name='postlike'),
    path('<int:pk>/', views.photodetail, name='photo-detail'),
]