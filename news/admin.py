from django.contrib import admin
from .models import Category, News, Contact
# Register your models here.
admin.site.register(Category)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published_date", "status", "category"]
    list_filter = ["status", "published_date", "edited_date", "category"]
    prepopulated_fields = {"slug": ('title',)}
    date_hierarchy = "published_date"
    search_fields = ["title", "body"]
    ordering = ["status", "published_date"]


admin.site.register(Contact)
