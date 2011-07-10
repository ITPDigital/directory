
from itpdirectory import MAIN_INDUSTRY, SPECIFIC_INDUSTRY, INDUSTRY_MAIN_SPECIFIC_MAP
from django.http import Http404, HttpResponse
from django.utils import simplejson
from itpdirectory.models import Category
from django.core import serializers    

def industry_ajax_servant(request):
    #if not request.is_ajax():
    #    raise Http404


    if request.GET.has_key("main_ind_id"):
        main_ind_id = request.GET['main_ind_id']

        try:
            sub = INDUSTRY_MAIN_SPECIFIC_MAP[ int( main_ind_id ) ]  
            res = [ item for item in SPECIFIC_INDUSTRY if item[0] in sub ] 
            ret = { 'choices' : res, }             

        except:
            return HttpResponse( "Get Outta Here!" )


        return HttpResponse(simplejson.dumps( ret ), content_type="application/json")

    return HttpResponse( "Awkward request!" )

def category_ajax_servant(request):
    parent_cat = request.GET.get( "cat_id" )
    cat = Category.objects.filter( category__id=parent_cat)

    fields = ('name')
    response = serializers.serialize('json', cat, fields=fields  )

    return HttpResponse( response, content_type="application/json")
   
