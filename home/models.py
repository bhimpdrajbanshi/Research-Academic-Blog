from django.db import models

from wagtail.models import Page
from menu.models import MenuItem, SubMenuItem

class HomePage(Page):
    pass
    #   def get_context(self, request):
    #     main_menus = MenuItem.objects.all()
    #     menu_dict = {}

    #     for item in main_menus:
    #         subitems = SubMenuItem.objects.filter(parent_menu_page=item.title)
    #         menu_dict[item] = subitems

    #     context = {
    #         'menu_dict': menu_dict,
    # }
    #     return context