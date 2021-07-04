from .models import Category

# This Should Call settings.py
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
