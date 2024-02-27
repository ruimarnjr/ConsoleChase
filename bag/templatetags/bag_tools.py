from django import template

# Extracted from the Code Institute's Boutique Ado Walkthrough Project

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity