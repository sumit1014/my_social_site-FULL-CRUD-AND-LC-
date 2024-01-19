from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'blog'
urlpatterns = [
    path('add_Comment', views.Add_Comment, name="add_Comment"),
    path('',views.blog_home,name="blog_home"),
    path('my_blogs',views.my_blogs,name="my_blogs"),
    path('createblog',views.createblog,name="createblog"),
    path('update<int:id>',views.updateblog,name="update"),
    path('delete<int:id>',views.deletepost,name="delete"),
    path('deletecomment<int:id>',views.deletecomment,name="deletecomment"),
    path('likes',views.postlike,name='postlike'),
    path('<slug:slug>/',views.blog_post,name="blog_post"),
]