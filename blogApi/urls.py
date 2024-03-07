from django.urls import path
from . import views



urlpatterns = [
 path('', views.BlogPostListView.as_view()),
 path('<str:slug>/detail/', views.BlogPostDetailView.as_view()),
 path('featured/', views.BlogPostFeaturedView.as_view()),
 path('category/', views.BlogPostCategoryView.as_view()),
 path('<str:slug>/', views.BlogPostDetailView.as_view()), 
]
