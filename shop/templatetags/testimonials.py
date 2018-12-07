from django import template
from django.template import Context
from shop.models import Testimonial
register = template.Library()

@register.simple_tag(takes_context=True)
def testimonial_tag(context, pizza):
    messages = Testimonial.objects.public_posts().filter(pizza=pizza)
    t = context.template.engine.get_template('shop/testimonials_list.html')
    return t.render(Context({'messages': messages},autoescape=context.autoescape))
