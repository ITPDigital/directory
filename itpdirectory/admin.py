from django.contrib import admin
from itpdirectory.models import Year, Directory, Magazine, Category, Brand, Company, Person, ManyCompanyPerson, ManyCompanyCompany, ManyDirectoryCompany  
import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.functional import curry
from datetime import datetime


class ManyDirectoryCompanyInline(admin.TabularInline):
    model = ManyDirectoryCompany
    extra = 1

class ManyCompanyPersonInline(admin.TabularInline):
    model =  ManyCompanyPerson
    extra = 1    



class ManyCompanyCompanyInline(admin.TabularInline):
    model =  ManyCompanyCompany
    fk_name = 'child' 
    extra = 1    

#class ManyBrandCompanyInline(admin.TabularInline):
#    model = ManyBrandCompany
#    extra = 1

class PersonAdmin(admin.ModelAdmin):
    list_display = ( '__unicode__' , 'nationality' , 'job_title' , 'job_function'  )
    list_filter = ( 'job_function', 'job_title' )
    inlines = ( ManyCompanyPersonInline,  )
    search_fields = ('first_name','last_name', )

    class Media:
        js = ( 
              settings.MEDIA_URL + "js/admin_forms.js", 
              )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'country', 'city', 'main_industry', 'specific_industry', 'person_link', 'persons',  )
    list_filter = ( 'status', 'is_active', 'main_industry',  'city', )
    inlines = ( ManyCompanyCompanyInline,  ManyDirectoryCompanyInline, )
    search_fields = ('name',)

    def add_view(self, request, extra_context=None):
        stamp = request.GET.get("pass")

        if not stamp:
            return HttpResponseRedirect("/admin/itpdirectory/company/")

        #compare the time stamp coming from the changelist if it's more than an hour redirect back. unix time.
        try:
            stamp_time = datetime.fromtimestamp(int( stamp ))
            delta = datetime.now() - stamp_time
            s = delta.seconds
            hours, remainder = divmod(s, 3600) 
            if hours > 0 or delta.days > 0: return HttpResponseRedirect("/admin/itpdirectory/company/")
        except:
            return HttpResponseRedirect("/admin/itpdirectory/company/")

        return super(CompanyAdmin, self).add_view(request, extra_context=extra_context)

    def changelist_view(self, request, extra_context=None):
        from django.utils.dateformat import format
        if not extra_context: extra_context = {}

        extra_context.update( { 'add_stamp' : format(datetime.now(), u'U') } )
        return super(CompanyAdmin, self).changelist_view(request, extra_context)


    class Media:
        js = ( 
              settings.MEDIA_URL + "js/admin_forms.js", 
              )

class DirectoryAdmin( admin.ModelAdmin ):
    list_display = ( 'name', 'main_industry', 'specific_industry', 'magazine',  )
    list_filter = ( 'main_industry', )

    class Media:
        js = ( 
              settings.MEDIA_URL + "js/admin_forms.js", 
              )

class CategoryAdmin( admin.ModelAdmin):
    list_display = ( 'name', 'category', )
    list_filter = (  'directory', )

admin.site.register( Year )
admin.site.register( Directory, DirectoryAdmin )
admin.site.register( Magazine )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Brand )
admin.site.register( Company, CompanyAdmin )
admin.site.register( Person, PersonAdmin )
