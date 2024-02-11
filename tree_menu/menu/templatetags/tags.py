from django import template
from ..models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None) -> dict:
    def create_menu(menu_item: str = None, submenu: list = None) -> list:
        menu = list(items.filter(parent=None)) if menu_item is None \
            else list(items.filter(parent__name=menu_item))

        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (TypeError, IndexError):
            pass
        try:
            return create_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return create_menu(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__name=menu_name)
    return {
        "menu": create_menu(),
    } if menu_name == menu_item \
        else {'menu': create_menu(menu_item)}