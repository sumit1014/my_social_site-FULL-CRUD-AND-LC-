from django.db import models
from django.db.models.signals import pre_save, post_save
from blog.utils import unique_slug_generator
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Post(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    blog_title = models.CharField(max_length=400)
    blog_content = models.TextField()
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    slug=models.SlugField(max_length=130,default='',blank=True,null=True)
    blog_post_time = models.DateTimeField(null=True, auto_now_add=True)
	
    
    def __str__(self):
        return self.blog_title

   
    def likecount(self):
        return self.likes.count()

    class Meta:
        ordering = ("-blog_post_time",)


def slug_generator_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator_save, sender=Post)

class blogComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_time = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username