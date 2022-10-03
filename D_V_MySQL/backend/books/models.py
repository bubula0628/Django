from django.db import models

class Books(models.Model):
    bookName = models.CharField(max_length=128)
    bookAuthor = models.CharField(max_length=45, blank=True, null=True)
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='創建時間')
