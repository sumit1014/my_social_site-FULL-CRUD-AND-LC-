from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Postphotos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    caption = models.CharField(max_length=1000,blank=True)
    image = models.ImageField(upload_to='images/',default='')
    image_post_time = models.DateTimeField(null=True, auto_now_add=True)
    like = models.ManyToManyField(User,blank=True,related_name='like')
    
    def __str__(self):
        return self.user.username

    def likecount(self):
        return self.like.count()
   
    class Meta:
        ordering = ("-image_post_time",)


class photoComment(models.Model):
    post = models.ForeignKey(Postphotos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_time = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username