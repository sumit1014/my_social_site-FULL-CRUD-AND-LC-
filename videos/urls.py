from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'videos'
urlpatterns = [
    path('add_Comment', views.Add_Comment, name="add_Comment"),
    path('',views.videos_home,name="videos_home"),
    path('my_videos',views.my_videos,name="my_videos"),  
    path('add_videos',views.add_videos,name="add_videos"),
    path('update<int:id>',views.updatevideopost,name="update"),
    path('delete_videos<int:id>',views.delete_videos,name="delete_videos"),
    path('deletecomment<int:id>',views.deletecomment,name="deletecomment"),
    path('like',views.postlike,name='postlike'),
    path('<int:pk>/', views.videodetail, name='video-detail'),
]