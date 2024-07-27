from django import template

from ..models import AdminMenu

register = template.Library()


@register.simple_tag()
def get_adminmenu(slug):
    return AdminMenu.objects.get(slug=slug)