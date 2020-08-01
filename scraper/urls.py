from django.urls import path, include
from .views import ScraperIndex, ArticleListView, ArticleDetailView, ArticleDeleteView


app_name = 'scraper'
urlpatterns = [
    path('', ScraperIndex.as_view()),
    path('list/', ArticleListView.as_view()),
    path('<int:pk>/', ArticleDetailView.as_view()),
    path('<int:pk>/delete/', ArticleDeleteView.as_view())
]
