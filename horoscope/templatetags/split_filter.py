from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter(name='russian_zodiac')
@stringfilter
def russian_zodiac(value, key=' '):
    split_dict = value.split(key)
    return split_dict[2]