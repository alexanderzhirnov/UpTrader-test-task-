from django import template
from django.urls import resolve, Resolver404
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    try:
        menu = Menu.objects.prefetch_related('items').get(slug=menu_name)
    except Menu.DoesNotExist:
        return {'menu': None}
    
    menu_items = menu.items.all()
    active_items = []
    
    # Находим активный пункт меню
    for item in menu_items:
        if item.get_url() == current_url:
            active_items.append(item)
    
    # Находим всех родителей активного пункта
    expanded_items = set()
    for item in active_items:
        parent = item.parent
        while parent:
            expanded_items.add(parent.id)
            parent = parent.parent
    
    # Собираем дерево меню
    def build_menu_tree(items, parent=None):
        result = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, item)
                result.append({
                    'item': item,
                    'children': children,
                    'is_expanded': item.id in expanded_items or item in active_items or any(
                        child['is_expanded'] for child in children
                    ),
                    'is_active': item in active_items,
                })
        return result
    
    menu_tree = build_menu_tree(menu_items)
    
    return {
        'menu': menu,
        'menu_tree': menu_tree,
        'current_url': current_url,
    }