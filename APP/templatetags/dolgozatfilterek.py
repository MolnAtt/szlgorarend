from django import template
# from datetime import datetime
from babel.dates import format_date, format_datetime, format_time

register = template.Library()

@register.filter(name='szep_szazalek')
def szep_szazalek(szam):
    if (szam.is_integer()):
        return f'{int(szam)}%'
    return f'{szam}%'

@register.filter(name='bol')
def bol(mibol, mit):
    return mibol - mit

@register.filter(name='ehn')
def ehn(datum):
    return format_datetime(datum, "yyyy.MM.dd (EEEE)", locale='hu_HU')
    # return datum.strftime('%Y.%m.%d (%a)')
