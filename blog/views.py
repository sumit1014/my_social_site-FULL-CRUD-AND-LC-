from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib import messages 
from django.contrib.auth.models import User 
from blog.models import Post,blogComment
from .forms import updateBlogpostform
# Create your views here.
def blog_home(request): 
    allPosts=Post.objects.all()
    context1={'allPosts': allPosts}
    return render(request, "blog/bloghome.html", context1)

def blog_post(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments= blogComment.objects.filter(post=post)
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        is_liked=True
    else:
        is_liked=False
    context2 = {'post': post,'comments': comments, 'user': request.user, 'is_liked':is_liked, 'total_likes':post.likecount()}
    return render(request, "blog/blog_post.html", context2) 

def createblog(request):
    if request.method == "POST":
        blog_title=request.POST.get("blog_title")
        blog_content=request.POST.get("blog_content")
        author_name=request.user
        post=Post(blog_title=blog_title, blog_content=blog_content,author_name=author_name)
        post.save()
        messages.success(request, "Your Blog has been uploaded successfully")
        return redirect("blog:blog_home")

def my_blogs(request): 
    mypost = Post.objects.filter(author_name=request.user)
    context3 = {"mypost":mypost}
    return render(request, "blog/my_blogs.html",context3)

def updateblog(request,id): 
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = updateBlogpostform(request.POST or None,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author_name = request.user
            post.save()
            messages.success(request, "Your Blog has been updated successfully")
            return redirect("blog:my_blogs")
    else:
        form = updateBlogpostform(instance=post)
        return render(request, "blog/update_blog.html", {'form': form})

def deletepost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request, "Your Blog has been deleted successfully")
    return redirect("blog:my_blogs")

def Add_Comment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(id=postSno)
        comment=blogComment(comment= comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been posted successfully")    
    return redirect(f"/blog/{post.slug}")

def deletecomment(request, id):
    delete_comment = blogComment.objects.get(id=id)
    delete_comment.delete()
    messages.success(request, "Your comment has been deleted successfully")
    return redirect("blog:blog_home")

def postlike(request):
    if request.method == 'POST':
        post=get_object_or_404(Post,id=request.POST.get('post_id'))
        is_liked=False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked=False
        else:
            post.likes.add(request.user)
            is_liked=True

    return redirect(f"/blog/{post.slug}")