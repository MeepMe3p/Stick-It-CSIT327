from django import template
from mainApp.utils import get_user_initials

register = template.Library()

@register.filter
def user_initials(user):
    return get_user_initials(user)
