from django.db import models

# Create your models here.

class Post(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=100, blank= True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

class comments(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    body = models.CharField(max_length=100,blank=False)
    owner = models.ForeignKey('auth.User' , related_name='comments', on_delete = models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

# Here, the ManyToManyField class creates a many-to-many relationship between the current model and the model indicated in the first argument. 
class Category(models.Model):

    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'
