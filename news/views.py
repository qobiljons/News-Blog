from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, UpdateView, DeleteView
from .forms import ContactForm

from .models import News, Category


# from .forms import MessageForm


# Create your views here.


class HomePageView(ListView):
    model = News
    template_name = "index.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # All news

        context["news"] = News.objects.filter(status=News.Status.Published)
        # Top Seen

        context["top_news"] = News.objects.filter(status=News.Status.Published)[:3]

        # The latest news

        context["latest_news"] = News.objects.order_by("-published_date")[:5]
        # Categories

        context["category_list"] = Category.objects.all()

        return context


def news_detail(request, news):
    detailed_news = get_object_or_404(News, slug=news)
    context = {
        "article": detailed_news
    }
    return render(request, template_name="article.html", context=context)


# def contact_page_view(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("Thank you!")
#     context = {
#         "form": form
#     }
#     return render(request, template_name="contact.html", context=context)
#

class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("Thank you!")
        context = {
            "form": form
        }
        return render(request, template_name=self.template_name, context=context)


class UserPageView(ListView):
    model = News
    template_name = "user.html"


def category_page_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    category_based_news = News.objects.filter(category=category)

    if not category_based_news.exists():
        context = {
            "error": "No articles found!"
        }
        return render(request, "404.html", context=context)

    context = {
        "category_name": category,
        "category_news": category_based_news
    }

    return render(request, "category.html", context=context)


class NewsUpdateView(UpdateView):
    model = News
    fields = "__all__"
    template_name = "update_news.html"


class NewsDeleteView(DeleteView):
    model = News
    template_name = "delete_news.html"
    success_url = reverse_lazy('home_page_view')


