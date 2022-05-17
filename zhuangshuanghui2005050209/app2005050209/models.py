from django.db import models
from uuslug import slugify
# Create your models here.
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=128,unique=True)
    count=models.IntegerField(default=0)
    slug=models.SlugField(blank=True)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类")
    title=models.CharField(max_length=128,verbose_name="标题")
    content=models.CharField(max_length=1024,blank=True,verbose_name="内容")
    

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    iphon=models.CharField(max_length=12,unique=True,verbose_name="手机号码")
    sex=models.CharField(max_length=20,verbose_name="性别")
    
    occupation=models.CharField(max_length=20,blank=True,verbose_name="职业")
    birthday=models.DateField(max_length=20,blank=True,verbose_name="生日")
    education=models.CharField(max_length=20,blank=True,verbose_name="教育程度")

    def __str__(self):
    	return self.user.username
