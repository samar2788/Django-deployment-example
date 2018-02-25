from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """

    This custs out all the values of ar fro string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
