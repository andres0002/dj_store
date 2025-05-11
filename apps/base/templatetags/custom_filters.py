# py
# django
from django import template
# third
# own

register = template.Library()

@register.filter
def startswith(value, arg):
    """Returns True if value (string) starts with arg."""
    if isinstance(value, str):
        return value.startswith(arg)
    return False