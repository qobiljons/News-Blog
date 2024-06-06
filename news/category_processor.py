from .models import Category, News


def get_category(request):
    categories = Category.objects.all()


    context = {
        "category_list": categories,
    }
    return context
