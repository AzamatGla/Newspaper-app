from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleEditView, ArticleDeleteView, ArticleCreateView
from . import views

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', ArticleEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('comment/', views.create_comment_view, name='comment'),
    path('', ArticleListView.as_view(), name='article')
]