from django.urls import path, include
from .views import ScraperIndex, ArticleListView


app_name = 'scraper'
urlpatterns = [
    path('', ScraperIndex.as_view()),
    path('list/', ArticleListView.as_view()),
]
