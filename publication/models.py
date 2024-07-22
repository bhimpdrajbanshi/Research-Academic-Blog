from django.db import models
from wagtail.models import Page

# Create your models here.
class Publication(Page):
    template = "publication/publication_page.html"
    pass