from django.db import models

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

class Entry(models.Model):
    """学到的关于某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        return f"{self.text[:50]}..."
# Create your models here.
