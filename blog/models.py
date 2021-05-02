from django.db import models

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    summary=models.CharField(max_length=100)

    def __str__(self):
        return self.title + " by " + self.author






