from django.urls import path
from . import views

urlpatterns = [
    #TODO add path to users endpoint
    path('article/create/', views.ArticleCreateView.as_view()),
    path('article/', views.ArticleListView.as_view()),
    path('article/<int:pk>/', views.ArticleDetailView.as_view()),
    path('article/<int:pk>/update/', views.ArticleUpdateView.as_view()),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view()),
    path('comments/', views.CommentListCreateView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('categories/', views.CategoryView.as_view()),
]