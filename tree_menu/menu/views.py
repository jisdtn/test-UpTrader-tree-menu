from django.shortcuts import render

from .models import Menu


def index(request):
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def draw_menu(request, path):
    modified_path = path.split('/')
    assert len(modified_path) > 0, 'draw_menu function has an error'
    context = {
        'menu_name': modified_path[0],
        'menu_item': modified_path[-1],
    }
    return render(
        request, 'menu/index.html', context
    )
