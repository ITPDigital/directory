from django.contrib import admin
from itpdirectory.models import Year, Directory, Magazine, Category, Brand, Company, Person, PersonBio, ManyCompanyPerson, ManyCompanyCompany, ManyDirectoryCompany  
import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.functional import curry
from datetime import datetime
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse


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





class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register( Year )
admin.site.register( Directory, DirectoryAdmin )
admin.site.register( Magazine )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Brand )
admin.site.register( Company, CompanyAdmin )
admin.site.register( Person, PersonAdmin )
admin.site.register( PersonBio )
