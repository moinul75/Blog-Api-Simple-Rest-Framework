from django.urls import path
from .views import (
    TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView,
    ImageListCreateAPIView, ImageRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView,
    BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView,
    ReactionListCreateAPIView, ReactionRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView,
    ReplyListCreateAPIView, ReplyRetrieveUpdateDestroyAPIView,
    BlogReadingTimeListCreateAPIView, BlogReadingTimeRetrieveUpdateDestroyAPIView,
    BlogWatchTimeListCreateAPIView, BlogWatchTimeRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),
    path('images/', ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageRetrieveUpdateDestroyAPIView.as_view(), name='image-detail'),
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-detail'),
    path('reactions/', ReactionListCreateAPIView.as_view(), name='reaction-list-create'),
    path('reactions/<int:pk>/', ReactionRetrieveUpdateDestroyAPIView.as_view(), name='reaction-detail'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('replies/', ReplyListCreateAPIView.as_view(), name='reply-list-create'),
    path('replies/<int:pk>/', ReplyRetrieveUpdateDestroyAPIView.as_view(), name='reply-detail'),
    path('blog-reading-times/', BlogReadingTimeListCreateAPIView.as_view(), name='blog-reading-time-list-create'),
    path('blog-reading-times/<int:pk>/', BlogReadingTimeRetrieveUpdateDestroyAPIView.as_view(), name='blog-reading-time-detail'),
    path('blog-watch-times/', BlogWatchTimeListCreateAPIView.as_view(), name='blog-watch-time-list-create'),
    path('blog-watch-times/<int:pk>/', BlogWatchTimeRetrieveUpdateDestroyAPIView.as_view(), name='blog-watch-time-detail'),
]

