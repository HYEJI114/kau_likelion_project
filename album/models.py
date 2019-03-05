from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    cover = models.ImageField(upload_to = 'images/')
    review = models.TextField()
    #rates = models.ChoiceField(choices=[(1,'★'), (2,'★★'), (3,'★★★'), (4,'★★★★'), (5,'★★★★★')])
    release_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title
