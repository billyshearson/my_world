from django.views.generic import TemplateView, ListView
from .models import Article


class ScraperIndex(TemplateView):
    template_name = "scraper/index.html"


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "scraper/article_list.html"
