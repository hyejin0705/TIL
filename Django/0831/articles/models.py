from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 10)   # 길이 제한 있음
    content = models.TextField()    # 길이 제한 없음

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


