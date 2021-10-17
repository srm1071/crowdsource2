from django.db import models

# Create your models here.

class Register(models.Model):
    first= models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    email= models.EmailField()
    depa= models.TextField(default=None)
    cor1x= models.PositiveIntegerField()
    cor1y= models.PositiveIntegerField()
    cor1st=models.TextField()
    cor1ed=models.TextField()
    rate1= models.PositiveIntegerField()
    reason1=models.TextField()
    cor2x= models.PositiveIntegerField()
    cor2y= models.PositiveIntegerField()
    cor2st=models.TextField()
    cor2ed=models.TextField()
    rate2= models.PositiveIntegerField()
    reason2=models.TextField()
    cor3x= models.PositiveIntegerField()
    cor3y= models.PositiveIntegerField()
    cor3st=models.TextField()
    cor3ed=models.TextField()
    rate3= models.PositiveIntegerField()
    reason3=models.TextField()
    gender=models.TextField()
    age=models.PositiveIntegerField()
    trans=models.TextField()

    def __str__(self):
        return self.first+" "+self.last
