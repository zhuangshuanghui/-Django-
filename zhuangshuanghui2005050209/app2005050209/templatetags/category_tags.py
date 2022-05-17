from django import template
from app2005050209.models import Category

register=template.Library()

@register.inclusion_tag('categorytab.html')
def category_tags():
    return {'categories':Category.objects.all()}