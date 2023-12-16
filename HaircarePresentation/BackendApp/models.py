from django.db import models

# Create your models here.

class HairTypeDB(models.Model):
    Hair_name = models.CharField(max_length=50, null=True, blank=True)
    Hair_des = models.CharField(max_length=100, null=True, blank=True)
    Hair_image = models.ImageField(upload_to="category", null=True, blank=True)

class HairproblemDB(models.Model):
    hair_prblm = models.CharField(max_length=50, null=True, blank=True)
    hairprblm_de = models.CharField(max_length=50, null=True, blank=True)
    prblm_image = models.ImageField(upload_to="prod", null=True, blank=True)


class HairBrandDB(models.Model):
    hairbrand_name = models.CharField(max_length=50, null=True, blank=True)
    hairbrand_img = models.ImageField(upload_to="brand", null=True, blank=True)



class Product_typeDB(models.Model):
    product_name = models.CharField(max_length=50,null=True,blank=True)
    product_des = models.CharField(max_length=50,null=True,blank=True)
    Product_img = models.ImageField(upload_to="pro",null=True,blank=True)

class AddproductDB(models.Model):
    Hairtype_name = models.CharField(max_length=50,null=True,blank=True)
    Problem_name = models.CharField(max_length=50,null=True,blank=True)
    Producttype_name = models.CharField(max_length=50,null=True,blank=True)
    Brand_name = models.CharField(max_length=50,null=True,blank=True)
    Product_name = models.CharField(max_length=50,null=True,blank=True)
    Product_des = models.CharField(max_length=50,null=True,blank=True)
    Prize = models.IntegerField(null=True,blank=True)
    Image = models.ImageField(upload_to="addpro",null=True, blank=True)
