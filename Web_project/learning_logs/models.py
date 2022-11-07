from django.db import models
class Topic(models.Model):
    """user learn topic"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的"""
        return self.text
# Create your models here.
