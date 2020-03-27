from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.timezone import now


class Article(models.Model):
    title = models.CharField(max_length=100,blank=False,verbose_name="标题")
    content = RichTextField(verbose_name="内容")
    def get_absulute_url(self):
        url = reverse(
            "Comment_blog:articleDetail",kwargs={
                "pk":self.pk,
                "title":self.title
            }
        )
        return url
    def __str__(self):
        return self.title
class Comments(models.Model):
    article = models.ForeignKey("Article",on_delete=models.CASCADE)
    comment = RichTextField(verbose_name="评论内容")
    ctime = models.DateTimeField(verbose_name="发表时间",default=now)
    parent = models.ForeignKey("Comments",related_name="reply",verbose_name="回复",null=True,blank=True,on_delete=models.PROTECT)
    def __str__(self):
        return self.comment