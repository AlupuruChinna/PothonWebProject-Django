from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model


class Prod(models.Model):
    product_name = models.CharField(max_length=200)
    product_desc = models.TextField()
    product_pubdate = models.DateTimeField()
    product_url = models.TextField(max_length=150)
    product_image = models.ImageField(upload_to="images/")
    product_by = models.ForeignKey(User,on_delete=models.CASCADE)
    product_likes = models.IntegerField(default=0)
    product_dislikes = models.IntegerField(default=0)



    def __str__(self):
        return self.product_name

    def prodsumm(self):
        return self.product_desc[0:100]

