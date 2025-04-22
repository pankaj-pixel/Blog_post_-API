from django.db import models


Status =(

    ('Draft','Draft'),
    ('Published','Published')
)
# Create your models here.
class Blog(models.Model):


    Blog_title = models.CharField(max_length=100)

    Content  = models.TextField()

    Author  = models.CharField(max_length=100)

    Created_at = models.DateTimeField()

    Status = models.CharField(choices=Status)

    def __str__(self):
        return self.Blog_title
