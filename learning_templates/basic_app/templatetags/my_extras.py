from django import template

register = template.Library()


@register.filter(name="rm_part")
def rm_part(value,arg):
    """
    This cuts out all values of arg from string(value)!
    """
    return value.replace(arg,'')

# register.filter('rm_part',rm_part)
