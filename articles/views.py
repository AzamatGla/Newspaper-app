from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = 'article/article_list.html'
    model = Article
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article/article_detail.html'
    login_url = 'login'


class ArticleEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'article/article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article/article_delete.html'
    success_url = reverse_lazy('article')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article/article_create.html'
    model = Article
    fields = ('title', 'body')
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def create_comment_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            article = Article.objects.get(id=form.cleaned_data['article'])
            Comment.objects.create(comment=comment, article=article, author=request.user)
            return redirect(reverse('article'))


