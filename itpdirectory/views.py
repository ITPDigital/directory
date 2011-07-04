
from itpdirectory import MAIN_INDUSTRY, SPECIFIC_INDUSTRY, INDUSTRY_MAIN_SPECIFIC_MAP
from django.http import Http404, HttpResponse
from django.utils import simplejson


def industry_ajax_servant(request):
    #if not request.is_ajax():
    #    raise Http404

    from django.core import serializers

    if request.GET.has_key("main_ind_id"):
        main_ind_id = request.GET['main_ind_id']

        if 1:
            sub = INDUSTRY_MAIN_SPECIFIC_MAP[ int( main_ind_id ) ]  
            res = [ item for item in SPECIFIC_INDUSTRY if item[0] in sub ] 
            ret = { 'choices' : res, }             

        #except:
        #    return HttpResponse( "Get Outta Here!" )

        #response = serializers.serialize('json', ret  )
        #return HttpResponse( response , content_type="application/json")

        return HttpResponse(simplejson.dumps( ret ), content_type="application/json")

    return HttpResponse( "Awkward request!" )
