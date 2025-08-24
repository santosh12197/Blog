from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Post
from django.views import View


class PostListView(View):
    def get(self, request):
        all_posts = Post.objects.all().order_by("-date_posted")

        # Create paginator with 3 posts per page
        paginator = Paginator(all_posts, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            "posts": page_obj
        }
        return render(request, "blog/home.html", context)


class UserPostListView(View):
    def get(self, request, author_id):
        user_posts = Post.objects.filter(author_id=author_id).order_by("-date_posted")
        author = user_posts.first().author.username

        # Create paginator with 3 posts per page
        paginator = Paginator(user_posts, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "posts": page_obj,
            "author": author,
            "user_posts_count": user_posts.count()
        }
        return render(request, "blog/user_posts.html", context)


class PostDetailView(View):
    def get(self, request, id):
        post = Post.objects.filter(id=id).first()
        if not post:
            return render(request, "blog/post_detail.html", {
                "error": "Sorry, the requested post does not exist."
            })
        context = {
            "post": post
        }
        return render(request, "blog/post_detail.html", context)


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "blog/post_form.html")
    
    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            return redirect("post-detail", id=post.id)  # redirect to detail page

        # If validation fails, re-render form with error
        context = {"error": "Both title and content are required."}
        return render(request, "blog/post_form.html", context)


class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        post = Post.objects.filter(id=id).first()
        if not post:
            return render(request, "blog/post_detail.html", {
                "error": "Sorry, the requested post does not exist."
            })
        context = {
            "post": post
        }
        return render(request, "blog/post_update.html", context)
    
    def post(self, request, id):
        post = get_object_or_404(Post, id=id)

        if request.user != post.author:
            messages.error(request, "Sorry, you can updated your own blog post only!")
            return render(request, "blog/post_update.html", {"post": post})
        
        # Get updated data from form
        title = request.POST.get("title")
        content = request.POST.get("content")

        # Update values
        post.title = title
        post.content = content
        post.save()

        # Redirect to detail page after saving
        return redirect("post-detail", id=post.id)


class PostDeleteView(View):
    def post(self, request, id):
        post = get_object_or_404(Post, id=id)

        if post.author != request.user:
            messages.error(request, "You can delete only your own posts!")
            return redirect("post-detail", id=post.id)

        post.delete()
        messages.success(request, f"Post {post.title} deleted successfully!")
        return redirect("blog-home")  # redirect to home or post list


class AboutView(View):
    def get(self, request):
        return render(request, "blog/about.html", {"title": "About"})
