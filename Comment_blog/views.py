from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView, DetailView, View

from Comment_blog.forms import ArticleForm, CommentsEditForm
from Comment_blog.models import Article, Comments


class CommentsEditView(FormView):
    form_class = CommentsEditForm

    def form_valid(self, form):
        comment = form.save()
        url = form.cleaned_data["article"].get_absulute_url()
        return HttpResponseRedirect(url)
class ArticleEditView(FormView):
    form_class = ArticleForm
    @csrf_exempt
    def form_valid(self, form):
        article = form.save()
        article.save()
        url = reverse("Comment_blog:index")
        return HttpResponseRedirect(url)
class ArtticleDetailView(DetailView):
    model = Article
    template_name = "articleDetail.html"
    context_object_name = "article"
    def get_comments(self,comment_list):
        from collections import OrderedDict
        comments_dict = {}
        header = []
        for comment in comment_list:
            comments_dict[comment] = []
            if comment.parent is None:
                header.append(comment)
            else:
                comments_dict[comment.parent].append(comment)
        return comments_dict,header
    def get_context_data(self, **kwargs):
        context = super(ArtticleDetailView,self).get_context_data(**kwargs)
        form = CommentsEditForm()
        form.fields["article"].initial = kwargs["object"].pk
        comments = Comments.objects.filter(article=kwargs["object"].pk)
        comment_dict,header = self.get_comments(comments)
        context["form"] = form
        context["comment_dict"] = comment_dict
        context["header"] = header
        return context

class IndexView(ListView):
    model = Article
    template_name = "index.html"
    context_object_name = "aritcles"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView,self).get_context_data(*kwargs)
        form = ArticleForm()
        context["form"] = form
        return context