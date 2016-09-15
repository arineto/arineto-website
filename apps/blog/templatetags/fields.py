from django import template

register = template.Library()

@register.inclusion_tag('blog/templatetags/_field.html')
def render_field(field):
    return {'field': field}
