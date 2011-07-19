from django.db import models
from itpdirectory import COMPANY_PERSON_RELATION,  COMPANY_COMPANY_RELATION, BRAND_COMPANY_RELATION, MAIN_INDUSTRY, SPECIFIC_INDUSTRY, PERSON_JOB_FUNCTION, COMPANY_TYPES, COMPANY_STATUS, STATE_TYPES
from itputils import LANGUAGES, COUNTRIES, CITIES
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.core.mail import mail_managers
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.conf import settings

class Year(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Magazine(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Directory(models.Model):
    name = models.CharField(max_length=255)
    year = models.ManyToManyField( Year )

    main_industry = models.IntegerField( choices=MAIN_INDUSTRY, default=1 )
    specific_industry = models.IntegerField( choices=SPECIFIC_INDUSTRY, default=1 )
    magazine = models.ForeignKey(Magazine)

    class Meta:
        verbose_name_plural = "Directories"
        ordering = ['name']

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Directories"

class Category(models.Model):
    name = models.CharField(max_length=255)
    directory = models.ForeignKey( Directory )
    category = models.ForeignKey("self", blank=True, null=True, related_name="child_category")

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=255)

    state = models.SmallIntegerField( choices=STATE_TYPES, default=0 )

    def __unicode__(self):
        return self.name

class Company(models.Model):
    title = models.CharField(max_length=255, help_text="This is only for internal system use to find this item.") #title this article just for internal use to distinguish article items.
    pobox = models.CharField(max_length=10)
    country = models.CharField( choices=COUNTRIES, max_length=5 )
    city = models.CharField( max_length=255 )
    zip_code =  models.CharField(max_length=5, blank=True, null=True)
    main_industry = models.IntegerField( choices=MAIN_INDUSTRY, default=1 )
    specific_industry = models.IntegerField( choices=SPECIFIC_INDUSTRY, default=1 )
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    email = models.EmailField()

    contact_person = models.CharField(max_length=255, blank=True, null=True,)
    contact_person_mobile = models.CharField(max_length=255, blank=True, null=True,)

    url = models.URLField( verify_exists=True, blank=True, null=True )
    facebook = models.CharField( max_length=255, blank=True, null=True )
    twitter = models.CharField(max_length=255, blank=True, null=True )
    logo = models.ImageField(upload_to='itpdirectory_company_logo',null=True,blank=True)

    state = models.IntegerField( choices=COMPANY_STATUS, default=1 )

    type = MultipleChoiceField( widget=CheckboxSelectMultiple, choices=COMPANY_TYPES )
    is_active = models.BooleanField()
   
    directory = models.ManyToManyField( Directory, null=True, blank=True, through="ManyDirectoryCompany", symmetrical=False, related_name='in_directories' )
    company = models.ManyToManyField( "self" , null=True, blank=True, through="ManyCompanyCompany", symmetrical=False, related_name='related_company' )
    brand = models.ManyToManyField( Brand, null=True, blank=True ) #, through="ManyBrandCompany" )

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def get_thumbnail(self):
        return None
        # i needs a logo
        #return self.image.url

    #location field
    lng = models.FloatField(verbose_name='latitude', blank=True, null=True, help_text="Please mark your location on the map below" )
    lat = models.FloatField(verbose_name='longitude', blank=True, null=True, help_text="Please mark your location on the map below" )
    zoom_level = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def person_link(self):
        return '<a href="%s?company=%s"> Add </a>' % ( reverse("admin:itpdirectory_person_add" ) , self.id  )

    person_link.allow_tags = True
    person_link.short_description = "Key Person" 

    def persons(self):
        people = self.person_set.all()
        string = ""
        for person in people:
            single = '<a href="%s"> %s </a> <br/>' % ( reverse("admin:itpdirectory_person_change", args=( person.id, ) ) , person  )
            string = "%s %s" % ( string, single ) 

        return string

    persons.allow_tags = True
    persons.short_description = "Existing Key Person" 

    def save(self, *args, **kwargs):
        email = True if not self.id else False

        super(Company, self).save(*args, **kwargs)

        if email:
            fail_silently = True if settings.DEBUG else False
            message = "Hey Ya ! A new company got added, check it out. ID is: %d" % self.id
            subject ="ITP Directory :: New company got added"
            mail_managers(subject, message, fail_silently )

    class Meta:
        verbose_name_plural = "Companies"


class CompanyTranslation(models.Model):
    company = models.ForeignKey( Company )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    language = models.IntegerField( choices=LANGUAGES, default=1 )

    def __unicode__(self):
        return self.name

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(help_text='Birth date format should be yyyy-mm-dd e.g. 1980-05-25', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % ( self.first_name , self.last_name )

class PersonBio(models.Model):
    #display fields
    title = models.CharField(max_length=255, help_text="To internally recognize this item in this system") #this overrides the previous for display purposes.
    name = models.CharField(max_length=255, help_text="How do you wish to display the guy's name this time?") #this overrides the previous for display purposes.
    nationality = models.CharField( choices=COUNTRIES, max_length=5, null=True, blank=True  )
    residence = models.CharField( choices=COUNTRIES, max_length=5, null=True, blank=True )
    email = models.EmailField(max_length=75, null=True, blank=True )
    job_title = models.CharField(max_length=255, null=True, blank=True)
    job_function = models.IntegerField( choices=PERSON_JOB_FUNCTION, null=True, blank=True )
    company = models.ManyToManyField( Company, through='ManyCompanyPerson', null=True, blank=True)
    biography = models.TextField( null=True, blank=True )
    language = models.IntegerField( choices=LANGUAGES, default=0 )

    person = models.ForeignKey( Person )

    def __unicode__(self):
        return "%s" % ( self.name )


class ManyCompanyPerson(models.Model):
    company = models.ForeignKey( Company )
    biography = models.ForeignKey( PersonBio )
    relation = models.IntegerField( choices=COMPANY_PERSON_RELATION, default=1 )
    directory = models.ManyToManyField( Directory  ) 

    def __unicode__(self):
        return mark_safe( "%s - %s" % ( self.company, self.person )  )


class ManyDirectoryCompany(models.Model):
    company = models.ForeignKey( Company )
    year = models.ForeignKey( Year ) 
    directory = models.ForeignKey(Directory)
    category = models.ForeignKey( Category, related_name="directory_company_category" )
    subcategory = models.ForeignKey( Category, related_name="directory_company_sub_category" )

    class Meta:
        verbose_name_plural = "Directories"


class ManyCompanyCompany(models.Model):
    company = models.ForeignKey( Company, null=True, blank=True, related_name='related_from' )
    related_to = models.ForeignKey( Company, null=True, blank=True, related_name='related_to' )
    relation = models.IntegerField( choices=COMPANY_COMPANY_RELATION, default=1 )

    class Meta:
        verbose_name_plural = "Company Relations"
        unique_together = ('company', 'related_to',)


    
