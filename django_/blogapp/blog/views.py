from django.shortcuts import render
from blog.models import Blog

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Komple Uygulamalı Web Geliştirme Eğitimi",
            "description": "Sıfırdan ileri seviyeye 'Web Geliştirme': Html, Css, Sass, Flexbox, Bootstrap, Javascript, Angular,JQuery, Asp.Net Mvc&Core Mvc",
            "img_url": 'blog/images/1.jpg'
        },
        {
            "id": 2,
            "title": "Python ile Sıfırdan İleri Seviye Python Programlama",
            "description": "Sıfırdan İleri Seviye Python Dersleri.Veritabanı,Veri Analizi,Bot Yazımı,Web Geliştirme(Django)",
            "img_url": 'blog/images/2.jpg'
        },
        {
            "id": 3,
            "title": "Sıfırdan İleri Seviye Modern Javascript Dersleri ES7+",
            "description": " Modern javascript dersleri ile (ES6 & ES7+) Nodejs, Angular, React ve VueJs için sağlam bir temel oluşturun.",
            "img_url": 'blog/images/3.jpg'
        },
        {
            "id": 4,
            "title": "Sıfırdan Uygulamalı React Geliştirme: Hooks, Redux & Firebase",
            "description": "SEn popüler frontend kütüphanesi React'i baştan sona uygulamalı projelerle öğren. Hooks,Redux, Webpack, Firebase ve Fazlası.",
            "img_url": 'blog/images/4.jpg'
        }
    ]
}

# Create your views here.


def index(request):
    context = {"blogs": Blog.objects.all(), "title": "Home"}
    return render(request, "blog/index.html", context)


def get_blogs(request):
    context = {"blogs": Blog.objects.all(), "title": "Blogs"}
    return render(request, "blog/blogs.html", context)


def get_blog_details(request, id: int):
    blog = Blog.objects.get(id=id)
    return render(request, "blog/blog_details.html", {"blog": blog, "title": blog.title})
