from django import template

from app_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: dict, menu_name: str) -> dict:
    menu_items: list = MenuItem.objects.filter(menu__name=menu_name).values()

    current_path: str = context.get('request', None).path

    menu_tree: list[dict] = values_list_to_tree(menu_items)

    def mark_active_items(menu_tree, url, parent_list=None):
        if parent_list is None:
            parent_list = []

        for item in menu_tree:
            if item['url'] == url:
                item['is_active'] = True
                for parent in parent_list:
                    parent['is_active'] = True
                return True

            if mark_active_items(item.get('children', []), url, parent_list + [item]):
                return True

        return False

    mark_active_items(menu_tree, current_path)

    context = {'menu': menu_tree}
    return context


def values_list_to_tree(values_list):
    items_by_id = {item['id']: {**item, 'children': []} for item in values_list}

    tree = []
    for item in items_by_id.values():
        parent_id = item['parent_id']
        if parent_id is None:
            tree.append(item)
        else:
            parent = items_by_id.get(parent_id)
            if parent:
                parent['children'].append(item)

    return tree



