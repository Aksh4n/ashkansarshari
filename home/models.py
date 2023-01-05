from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)



    def __str__(self):

        return self.subject  


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    ticket = models.TextField(max_length=1000)



    def __str__(self):

        return self.email  
class ViewCount(models.Model):
    a = models.IntegerField(null=True)   
    def __str__(self):

        return str(self.a)      

class Category(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    image = models.ImageField(null=True,blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url            
