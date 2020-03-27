from django import forms
from django.forms import ModelForm

from Comment_blog.models import Article, Comments


class ArticleForm(ModelForm):
    title = forms.CharField(max_length=100,required=True)
    class Meta:
        model = Article
        fields = ["title","content"]
        widgets = {
            "title":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"title"
            }),
            "content":forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "文章内容"
                }
            )
        }
class CommentsEditForm(ModelForm):

    class Meta:
        model = Comments
        fields = ["article","comment","parent"]
        widgets = {
            "article":forms.HiddenInput(
            ),
            "comment":forms.Textarea(
                attrs={
                    "cols":"80",
                    "rows":"10",
                    "class":"form-controlo",
                    "placeholder":"请输入你的评论",
                    "style":"outline:none"
                }
            ),
            "parent":forms.HiddenInput(
                attrs={
                    "id":"c_id"
                }
            )
        }