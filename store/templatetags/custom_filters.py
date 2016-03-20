from django import template

register= template.Library()

@register.filter(name='to_cents')
def to_cents(value):
    return int(value * 100)

@register.filter(name='pluralize')
def pluralize(value):
    retval = ""
    if value > 1:
        retval = "s"	
	return retval