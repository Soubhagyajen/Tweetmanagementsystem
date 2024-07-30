from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=230)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now= True)  

    class Meta:
        unique_together = ('user', 'tweet')

    def __str__(self):
        return f"{self.user} likes {self.tweet}"    

