from django.db import models

# Create your models here.
class Posts(models.Model):
    id=models.AutoField(primary_key=True)
    post_title:models.CharField(max_length=225)
    post_description=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    objects=models.Manager()