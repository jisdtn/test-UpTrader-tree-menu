# from django import template
# from ..models import MenuItem
#
# register = template.Library()
#
# @register.inclusion_tag('menu.html', takes_context=True)
# def create_menu(contex):
#     menu_items = MenuItem.objects.all()
#     return {
#         "menu_items": menu_items,
#     }