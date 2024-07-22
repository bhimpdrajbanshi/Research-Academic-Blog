from django import template

from ..models import Menu

register = template.Library()


@register.simple_tag()
def get_menu(slug):
    print('55555')
    return Menu.objects.get(slug=slug)