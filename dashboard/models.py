from wagtail.models import Page
from menu.models import MenuItem, SubMenuItem
from menu.models import Pages, AccessPages

class Dashboard(Page):
    template = "admin/dashboard.html"
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