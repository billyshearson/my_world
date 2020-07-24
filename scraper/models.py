from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    src = models.URLField()
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
