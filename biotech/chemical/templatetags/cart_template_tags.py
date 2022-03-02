from django import template
from chemical.models import Request

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        qs = Request.objects.filter(user=user, requested=False)
        if qs.exists():
            return qs[0].chemicals.count()
    return 0
