from django.db import models
from wagtail.models import Page

class BlogIndex(Page):
    template = "blog_index_page.html"
    pass
class BlogDetails(Page):
    template = "blog/blog_details_page.html"
    pass