from django import template

register = template.Library()


@register.filter
def str_count(s, i):
    return s.count(i)

