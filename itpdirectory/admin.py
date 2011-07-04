from django.contrib import admin
from itpdirectory.models import Year, Directory, Magazine, Category, Brand, Company, Person, ManyCompanyPerson, ManyCompanyCompany, ManyDirectoryCompany  
import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.functional import curry


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

    class Media:
        js = ( 
              settings.MEDIA_URL + "js/admin_forms.js", 
              )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'country', 'city', 'main_industry', 'specific_industry', 'person_link'  )
    list_filter = ( 'main_industry',  'city', )
    inlines = ( ManyCompanyCompanyInline,  ManyDirectoryCompanyInline, )

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
    list_filter = ( 'category', 'directory' )

admin.site.register( Year )
admin.site.register( Directory, DirectoryAdmin )
admin.site.register( Magazine )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Brand )
admin.site.register( Company, CompanyAdmin )
admin.site.register( Person, PersonAdmin )
