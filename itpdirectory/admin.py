from django.contrib import admin
from itpdirectory.models import Year, Directory, Magazine, Category, Brand, Company, CompanyTranslation, Person, PersonBio, ManyCompanyPersonBio, ManyCompanyCompany, ManyDirectoryCompany 
import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.functional import curry
from datetime import datetime
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse
from django import forms
from django.utils.dateformat import format
from django.contrib.localflavor.us.forms import USPhoneNumberField, phone_digits_re
from django.utils.encoding import smart_unicode
from django.forms.fields import EMPTY_VALUES
import re

from ajax_filtered_fields.forms import ManyToManyByLetter, ForeignKeyByRelatedField, ManyToManyByRelatedField

from itputils.autocomplete_admin import FkAutocompleteAdmin, InlineAutocompleteAdmin

phone_digits_re = re.compile(r'^(\d{3})\s(\d{1,2})\s(\d{7})$')

class PhoneNumberMultiWidget(forms.MultiWidget):
    """
    A Widget that splits US Phone number input into three  boxes.
    """
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone', 'style': 'margin-right:5px',}),
            forms.TextInput(attrs={'size':'2','maxlength':'2', 'class':'phone', 'style': 'margin-right:5px',}),
            forms.TextInput(attrs={'size':'7','maxlength':'7', 'class':'phone', 'style': 'margin-right:5px',}),
        )
        super(PhoneNumberMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None,None,None]

    def value_from_datadict(self, data, files, name):
        values = tuple(super(PhoneNumberMultiWidget, self).value_from_datadict(data, files, name))
        return u'%s %s %s' % values


class PhoneNumberField(USPhoneNumberField):
    def clean(self, value):
        if value in EMPTY_VALUES:
            return u''
        m = phone_digits_re.search(value)
        if m:
            print u'%s %s %s' % (m.group(1), m.group(2), m.group(3))
            return u'%s %s %s' % (m.group(1), m.group(2), m.group(3))
        raise forms.ValidationError("Phone numbers must be in 'int(3) local(1,2) number(7)' format and contain only numbers.")


class ManyDirectoryCompanyForm(forms.ModelForm):
    #directory = ForeignKeyByRelatedField(Directory, field_name="year", required=False,)
    #category = ForeignKeyByRelatedField(Category, field_name="directory", required=False,)
    #subcategory = ForeignKeyByRelatedField(Category, field_name="category", required=False,)

    class Meta:
        model = ManyDirectoryCompany


class ManyDirectoryCompanyInline(admin.TabularInline):
    model = ManyDirectoryCompany
    extra = 1
    form = ManyDirectoryCompanyForm
    template = "admin/itpdirectory/company/tabular.html"


class ManyCompanyPersonBioInline(admin.TabularInline):
    model =  ManyCompanyPersonBio
    extra = 1    


class ManyCompanyCompanyInline(InlineAutocompleteAdmin):
    model =  ManyCompanyCompany
    fk_name = 'company'
    extra = 1
    related_search_fields = {  'related_to': ('title',), }
    template = "admin/itpdirectory/company/tabular.html"

class CompanyTranslationInline(admin.TabularInline):
    model = CompanyTranslation
    extra = 1

class PersonBioAdmin(admin.ModelAdmin):
    list_display = ( '__unicode__' , 'nationality' , 'job_title' , 'job_function'  )
    list_filter = ( 'job_function', 'job_title' )
    inlines = ( ManyCompanyPersonBioInline,  )
    search_fields = ('name','title', )

    class Media:
        css = {
			'all': (settings.MEDIA_URL + "css/jquery-ui-1.8.14.custom.css",)
		}
        js = (
            settings.MEDIA_URL + "js/jquery-1.5.1.min.js",
            settings.MEDIA_URL + "js/jquery-ui-1.8.14.custom.min.js",
            settings.MEDIA_URL + "js/admin_forms.js",
        )


class CompanyAdminForm(forms.ModelForm):
    brand = ManyToManyByLetter(Brand, field_name="name", required=False,)
    phone = PhoneNumberField(label="Phone", widget=PhoneNumberMultiWidget())
    fax = PhoneNumberField(label="Fax", widget=PhoneNumberMultiWidget())
    contact_person_mobile = PhoneNumberField(label="Contact person mobile:", widget=PhoneNumberMultiWidget())

    class Meta:
        model = Company

    class Media:
        css = {
			'all': (settings.MEDIA_URL + "css/jquery-ui-1.8.14.custom.css",)
		}
        js = (
            settings.ADMIN_MEDIA_PREFIX + "js/SelectBox.js",
            settings.ADMIN_MEDIA_PREFIX + "js/SelectFilter2.js",
            settings.MEDIA_URL + "js/jquery-1.5.1.min.js",
            settings.MEDIA_URL + "js/jquery-ui-1.8.14.custom.min.js",
            settings.MEDIA_URL + "js/ajax_filtered_fields.js",
            settings.MEDIA_URL + "js/jquery.maskedinput-1.3.js",
            settings.MEDIA_URL + "js/admin_forms.js",
        )


class CompanyAdmin(FkAutocompleteAdmin):
    list_display = ( 'title', 'country', 'city_value', 'main_industry', 'specific_industry', 'person_link', 'persons', 'branch_link',  )
    list_filter = ( 'state', 'is_active', 'main_industry', 'city'  )
    ordering       = ( 'title', )
    search_fields = ('title',)

    filter_horizontal = ( 'brand', )

    inlines = [
        CompanyTranslationInline,
        ManyDirectoryCompanyInline,
        ManyCompanyCompanyInline,
    ]

    form = CompanyAdminForm

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

    def change_view(self, request, object_id, extra_context={}):
        extra_context.update( { 'add_stamp' : format(datetime.now(), u'U') } )
        return super(CompanyAdmin, self).change_view(request,object_id, extra_context)

    def changelist_view(self, request, extra_context={}):
        extra_context.update( { 'add_stamp' : format(datetime.now(), u'U') } )
        return super(CompanyAdmin, self).changelist_view(request, extra_context)


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
admin.site.register( CompanyTranslation )
admin.site.register( PersonBio, PersonBioAdmin )
admin.site.register( Person )
