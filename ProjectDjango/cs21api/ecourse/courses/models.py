from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    pass

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id']


class Category(BaseModel):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject
    class Meta:
        unique_together = ('subject', 'category')

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)


    def __str__(self):
        return self.name