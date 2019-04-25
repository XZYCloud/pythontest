from django.db import models

# Create your models here.
class Douban(models.Model):
    num=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    charactor=models.CharField(max_length=100)
    remark=models.CharField(max_length=100)
    score=models.CharField(max_length=100)

    def __str__(self):
        return self.name