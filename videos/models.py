from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Postvideos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    about_video = models.CharField(max_length=1000,blank=True)
    video = models.FileField(upload_to='videos/',default='')
    video_post_time = models.DateTimeField(null=True, auto_now_add=True)
    like_video = models.ManyToManyField(User,blank=True,related_name='like_video')
    
    def __str__(self):
        return self.user.username

    def likecount(self):
        return self.like_video.count()

    class Meta:
        ordering = ("-video_post_time",)

class videoComment(models.Model):
    post = models.ForeignKey(Postvideos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    comment_time = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username