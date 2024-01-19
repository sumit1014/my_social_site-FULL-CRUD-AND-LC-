from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User
from videos.models import Postvideos,videoComment
from .forms import videopostform,updatevideopostform
# Create your views here.

def videos_home(request):
    allPosts = Postvideos.objects.all()
    context1 = {'allPosts': allPosts}
    return render(request, "videos/videos_home.html",context1)

def my_videos(request): 
    mypost = Postvideos.objects.filter(user=request.user)
    context2 = {"mypost":mypost}
    return render(request, "videos/my_videos.html",context2)

def videodetail(request, pk):
    post = Postvideos.objects.get(pk=pk)
    comments = videoComment.objects.filter(post=post)
    is_liked=False
    if post.like_video.filter(id=request.user.id).exists():
        is_liked=True
    else:
        is_liked=False
    context3 = {'post': post,'comments': comments, 'user': request.user, 'is_liked':is_liked, 'total_likes':post.likecount()}
    return render(request, "videos/videos_detail.html", context3) 


def add_videos(request):
    if request.method == "POST":
        form = videopostform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post has been uploaded successfully")
            return redirect("videos:videos_home")
        else:
            # Display error messages if the form is not valid
            messages.error(request, "There was an error in the form submission. Please try again.")
    else:
        form = videopostform()
    return render(request, 'videos/videos_home.html', {'form': form})


def delete_videos(request, id):
    post = Postvideos.objects.get(id=id)
    post.delete()
    messages.success(request, "Your photo has been deleted successfully")
    return redirect("videos:my_videos")

def Add_Comment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Postvideos.objects.get(id=postSno)
        comment= videoComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")    
    return redirect(f"/videos/{post.pk}")

def deletecomment(request, id):
    delete_comment = videoComment.objects.get(id=id)
    delete_comment.delete()
    messages.success(request, "Your comment has been deleted successfully")
    return redirect("videos:videos_home")

def postlike(request):
    if request.method == 'POST':
        post=get_object_or_404(Postvideos,id=request.POST.get('post_id'))
        is_liked=False
        if post.like_video.filter(id=request.user.id).exists():
            post.like_video.remove(request.user)
            is_liked=False
        else:
            post.like_video.add(request.user)
            is_liked=True
    return redirect(f"/videos/{post.pk}")

def updatevideopost(request,id): 
    post = Postvideos.objects.get(id=id)
    if request.method == "POST":
        form = updatevideopostform(request.POST or None,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post has been updated successfully")
            return redirect("videos:my_videos")
    else:
        form = updatevideopostform(instance=post)
        return render(request, "videos/update_video_post.html", {'form': form})