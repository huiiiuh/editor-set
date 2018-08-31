from django.shortcuts import render, HttpResponse

from django.views.generic import View
from .models import Blog


class BlogDetailView(View):
    def get(self, request, blog_id):
        blog = Blog.objects.filter(id=blog_id).first()
        return render(request, "blog-detail.html", {"blog": blog})
