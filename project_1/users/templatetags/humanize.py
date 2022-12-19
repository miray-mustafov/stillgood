import re
from decimal import Decimal
from django import template
from django.utils.formats import number_format

register = template.Library()


@register.filter()
def intcomma(value, use_l10n=True):
    orig = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r"\g<1>,\g<2>", orig)
    if orig == new:
        return new
    else:
        return intcomma(new, use_l10n)

