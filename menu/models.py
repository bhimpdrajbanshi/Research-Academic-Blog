from django.db import models

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
from django.contrib.auth.models import User, Group
from wagtail.models import Page
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse

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

    page = ParentalKey("Menu", related_name="menu_items")

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

    page = ParentalKey("Menu", related_name="sub_menu_items")

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

    page = ParentalKey("Menu", related_name="third_menu_items")

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
class Menu(ClusterableModel):
    """The main menu clusterable model."""

    title = models.CharField(max_length=100)
    slug = models.CharField(editable=True)
    # slug = models.SlugField()

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu"),
        InlinePanel("menu_items", label="Menu"),
        InlinePanel("sub_menu_items", label="Sub Menu"),
        InlinePanel("third_menu_items", label="Third Menu"),
    ]

    def __str__(self):
        return self.title
    
  
class Pages(Orderable):
    link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.CASCADE,
    )
    page = ParentalKey("AccessPages", related_name="pages")

    panels = [
        PageChooserPanel("link_page"),
    ]

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        return '#'


class AccessPages(ClusterableModel, Orderable):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    page = ParentalKey("Privileges", related_name="page_access")

    panels = [
        FieldPanel("group"),
        InlinePanel("pages", label="Privileges Pages"),
    ]


@register_snippet
class Privileges(ClusterableModel):
    title = models.CharField(max_length=100)
    slug = models.CharField(editable=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Privileges"),
        InlinePanel("page_access", label="User Privileges"),
    ]

    def __str__(self):
        return self.title
    
    def get_accessible_pages(self, group):
        accessible_pages = []
        print(accessible_pages,'accessible_pages')
        for access_page in self.page_access.filter(group=group):
            for page in access_page.pages.all():
                accessible_pages.append(page.link_page.url)
        return accessible_pages
    


class RestrictedPage(Page):
    """
    A page model with restricted access based on user groups.
    """
    def serve(self, request, *args, **kwargs):
        allowed_groups = ['AccessGroup']
        
        if request.user.is_authenticated:
            user_groups = request.user.groups.values_list('name', flat=True)
            if not any(group in allowed_groups for group in user_groups):
                raise PermissionDenied("You do not have access to this page.")
        else:
            return redirect(reverse('login'))  # Redirect to login if user is not authenticated
        
        return super().serve(request, *args, **kwargs)
