from django.db import models
from wagtail.models import Page
from menu.models import MenuItem, SubMenuItem
from menu.models import Pages, AccessPages
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import (
    MultiFieldPanel,
    InlinePanel,
    FieldPanel,
    PageChooserPanel,
)
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet

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
    
    
    
class MenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("AdminMenu", related_name="menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'
    def __str__(self):
        return self.link_title
    
class SubMenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    parent_menu_page=models.ForeignKey(
        "MenuItem",on_delete=models.CASCADE,
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("AdminMenu", related_name="sub_menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("parent_menu_page"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'
    def __str__(self):
        return self.link_title

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'
    

class ThirdMenuItem(Orderable):

    link_title = models.CharField(
        blank=True,
        null=True,
        max_length=50
    )
    parent_Sub_menu_page=models.ForeignKey(
        "SubMenuItem",on_delete=models.CASCADE,
    )
    link_url = models.CharField(
        max_length=500,
        blank=True
    )
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    open_in_new_tab = models.BooleanField(default=False, blank=True)

    page = ParentalKey("AdminMenu", related_name="third_menu_items")

    panels = [
        FieldPanel("link_title"),
        FieldPanel("parent_Sub_menu_page"),
        FieldPanel("link_url"),
        PageChooserPanel("link_page"),
        FieldPanel("open_in_new_tab"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_url:
            return self.link_url
        return '#'

    @property
    def title(self):
        if self.link_page and not self.link_title:
            return self.link_page.title
        elif self.link_title:
            return self.link_title
        return 'Missing Title'


@register_snippet
class AdminMenu(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
    slug = models.CharField(editable=True)
    # slug = models.SlugField()

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="AdminMenu"),
        InlinePanel("menu_items", label="AdminMenu"),
        InlinePanel("sub_menu_items", label="Sub Menu"),
        InlinePanel("third_menu_items", label="Third Menu"),
    ]

    def __str__(self):
        return self.title
    
  