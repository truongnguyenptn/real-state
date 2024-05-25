from django.urls import path

from .views.blog import PostsGridView, PostDetailView
from .views.blog import PostCommentView, PostCommentDeleteView


urlpatterns = (
    path('', PostsGridView.as_view(), name='blog page'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post detail'),
    path('comment/<slug:slug>/', PostCommentView.as_view(), name='comment post'),
    path('delete-comment/<int:pk>/', PostCommentDeleteView.as_view(), name='delete comment'),
)
