from django.db import models
from wagtail.models import Page

# Create your models here.
class Research(Page):
    template = "research/research_page.html"
    pass