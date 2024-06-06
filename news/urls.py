from django.urls import path
from .views import (
    HomePageView,
    news_detail,
    UserPageView,
    ContactPageView,
    category_page_view,
    NewsUpdateView,
    NewsDeleteView,
    NewsCreateView)


urlpatterns = [
    path("", HomePageView.as_view(), name="home_page_view"),
    path("news/<slug:news>", news_detail, name="single_article_view"),
    path("user/", UserPageView.as_view(), name="user_page_view"),
    path("contact/", ContactPageView.as_view(), name="contact_page_view"),
    path("<str:category_name>/", category_page_view, name="category_page_view"),
    path("news/create/", NewsCreateView.as_view(), name="create_news_view"),
    path("news/<slug>/update", NewsUpdateView.as_view(), name="update_news_view"),
    path("news/<slug>/delete", NewsDeleteView.as_view(), name="delete_news_view"),
]

