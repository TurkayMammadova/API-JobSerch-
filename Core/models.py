from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
  name = models.CharField(max_length=100,null=True,blank=True)
  image = models.CharField(max_length=100, null=True,blank=True)
  slug=models.SlugField(max_length=255, db_index=True, null=True, unique=True, blank=True)
  
  
  def __str__(self):
    return str(self.name)
  
  def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Company(models.Model):
  name = models.CharField(max_length=100,null=True,blank=True)
  image = models.CharField(max_length=100, null=True,blank=True)
  description = models.TextField(null=True,blank=True)
  location =  models.CharField(max_length=150,null=True,blank=True)
  phone =  models.CharField(max_length=100,null=True,blank=True)
  website =  models.CharField(max_length=100,null=True,blank=True)
  slug = models.SlugField(max_length=255, db_index=True, null=True, unique=True, blank=True)
    
  def __str__(self):
    return str(self.name)
  
  def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
  
  
class ADS(models.Model):
  name = models.CharField(max_length=100,null=True,blank=True)
  category_id = models.ManyToManyField(Category)
  company_id = models.ForeignKey(Company,on_delete = models.CASCADE,null=True,blank=True)
  demands = models.TextField(null=True,blank=True)
  responsibilities = models.TextField(null=True,blank=True)
  conditions = models.TextField(null=True,blank=True)
  created_at = models.DateTimeField( auto_now_add=True)
  to_choose = models.BooleanField(default=False)
  views_count = models.IntegerField(default=0)
  email = models.CharField(max_length=100,null=True,blank=True)
  slug=models.SlugField(max_length=255, db_index=True, null=True, unique=True, blank=True)
  
  
  def __str__(self):
    return str(self.name)
  
  
  def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)