from django.urls import path

from . import views

# http://127.0.0.1:8000/         => index
# http://127.0.0.1:8000/index    => index
# http://127.0.0.1:8000/blogs/3  => blog-details.html
urlpatterns = [
    path("", views.index),
    path("index", views.index, name="home"),
    path("blogs", views.get_blogs, name="blogs"),
    path("blogs/<int:id>", views.get_blog_details, name="blog_details"),
    path("category/<slug:slug>", views.get_blogs_by_category,
         name="get_blogs_by_category")
]
