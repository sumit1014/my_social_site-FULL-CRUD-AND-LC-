from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User
from photos.models import Postphotos, photoComment
from .forms import photopostform,updatephotopostform
# Create your views here.
def photos_home(request):
    allPosts=Postphotos.objects.all()
    context1={'allPosts': allPosts}
    return render(request, "photos/photoshome.html",context1)

def my_photos(request): 
    mypost = Postphotos.objects.filter(user=request.user)
    context2 = {"mypost":mypost}
    return render(request, "photos/myphotos.html",context2)

def photodetail(request, pk):
    post =  Postphotos.objects.get(pk=pk)
    comments=  photoComment.objects.filter(post=post)
    is_liked=False
    if post.like.filter(id=request.user.id).exists():
        is_liked=True
    else:
        is_liked=False
    context3 = {'post': post,'comments': comments, 'user': request.user, 'is_liked':is_liked, 'total_likes':post.likecount()}
    return render(request, "photos/photos_detail.html", context3) 

def add_photos(request):
    if request.method == "POST":
        form = photopostform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post has been uploaded successfully")
            return redirect("photos:photos_home")
        else:
            # Display error messages if the form is not valid
            messages.error(request, "There was an error in the form submission. Please try again.")
    else:
        form = photopostform()
    return render(request, 'photos/photoshome.html', {'form': form})

def delete_photos(request, id):
    post = Postphotos.objects.get(id=id)
    post.delete()
    messages.success(request, "Your photo has been deleted successfully")
    return redirect("photos:my_photos")

def Add_Comment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Postphotos.objects.get(id=postSno)
        comment= photoComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")    
    return redirect(f"/photos/{post.pk}")

def deletecomment(request, id):
    delete_comment = photoComment.objects.get(id=id)
    delete_comment.delete()
    messages.success(request, "Your comment has been deleted successfully")
    return redirect("photos:photos_home")

def postlike(request):
    if request.method == 'POST':
        post=get_object_or_404(Postphotos,id=request.POST.get('post_id'))
        is_liked=False
        if post.like.filter(id=request.user.id).exists():
            post.like.remove(request.user)
            is_liked=False
        else:
            post.like.add(request.user)
            is_liked=True
    return redirect(f"/photos/{post.pk}")

def updatephotopost(request,id): 
    post = Postphotos.objects.get(id=id)
    if request.method == "POST":
        form = updatephotopostform(request.POST or None,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Your post has been updated successfully")
            return redirect("photos:my_photos")
    else:
        form = updatephotopostform(instance=post)
        return render(request, "photos/update_photo_post.html", {'form': form})