from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from .models import Article


class ScraperIndex(TemplateView):
    template_name = "scraper/index.html"


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "scraper/article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "scraper/article_detail.html"
    context_object_name = 'article'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "scraper/article_delete.html"
    context_object_name = 'article'
