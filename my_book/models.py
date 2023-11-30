from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):

    #name=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_name')
    name=models.CharField(max_length=100,verbose_name=_('name of author'))
    birth_date=models.DateField(default=datetime.datetime.now)
    biography=models.TextField(max_length=500)

    def __str__(self):
        return str(self.name)
    
class Book(models.Model):
    
    title=models.CharField(max_length=100,verbose_name=_('name_book'))
    author=models.ForeignKey(Author,on_delete=models.Case,related_name='book_author')
    publish_date=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Book,self).save(*args,**kwargs)
    
class Review(models.Model):
    rating=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]

    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review_book')
    review_name=models.CharField(max_length=100)
    conent=models.TextField(max_length=500)
    rate=models.CharField(max_length=20,choices=rating)

    rate2 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self(self.book)







