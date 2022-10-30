from django.contrib import admin
from .models import Blog, Category


# Create your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_editable = ("is_active",)
    list_filter = ("category",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
