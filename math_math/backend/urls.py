from django.urls import path

from backend import views

urlpatterns = [
    path('detail/<blog_id>/', views.BlogDetailView.as_view(), name="blog-detail")
]
