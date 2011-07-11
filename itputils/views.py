from itputils import COUNTRIES, CITIES, COUNTRIES_CITIES_MAP
from django.http import Http404, HttpResponse
from django.utils import simplejson
from itpdirectory.models import Category
from django.core import serializers    

def country_city_ajax_servant(request):
    country = request.GET.get( "country" )
    try:
        sub = COUNTRIES_CITIES_MAP[ country.upper() ]
        res = [ item for item in CITIES if item[0] in sub ] 
        ret = { 'choices' : res, }
        return HttpResponse(simplejson.dumps( ret ), content_type="application/json")

    except:
        return HttpResponse( "Get Outta Here!" )

    return HttpResponse( "Awkward request!" )


