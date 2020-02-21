from django.db import models

class User(models.Model):
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    password_hash=models.TextField()

    def __str__(self):
        return self.username

class Post(models.Model):
    title=models.CharField(max_length=300)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

