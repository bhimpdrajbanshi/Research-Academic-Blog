from django.db import models
from wagtail.models import Page
from menu.models import Pages, AccessPages

class BlogIndex(Page):
    template = "blog/blog_index_page.html"
    pass
class BlogDetails(Page):
    template = "blog/blog_details_page.html"
    def get_context(self, request):
        # Get all pages
        pages = Pages.objects.all()
        
        # Get all access pages
        access_pages = AccessPages.objects.all()

        # Call the superclass method to get the default context
        context = super().get_context(request)

        # Add your custom context variables
        context['access_pages'] = access_pages
        context['pages'] = pages
        
        return context