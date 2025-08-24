

from django.urls import path
# from . import views
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, AboutView, PostUpdateView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user_posts/<int:author_id>/', UserPostListView.as_view(), name="user-posts-list"),
    path('post/<int:id>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:id>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:id>/delete/', PostDeleteView.as_view(), name="post-delete"),

    path('about/', AboutView.as_view(), name="blog-about"),

]