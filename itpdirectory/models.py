from django.db import models
from itpdirectory import COMPANY_PERSON_RELATION,  COMPANY_COMPANY_RELATION, BRAND_COMPANY_RELATION, MAIN_INDUSTRY, SPECIFIC_INDUSTRY, PERSON_JOB_FUNCTION, COMPANY_STATUS
from itputils import COUNTRIES, CITIES
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.core.mail import mail_managers

from django.conf import settings

class Year(models.Model):
    name = models.CharField(max_length=255)

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

    def __unicode__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=255)
    directory = models.ForeignKey( Directory )
    category = models.ForeignKey("self", blank=True, null=True, related_name="child_category")
    
    def __unicode__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255)
    pobox = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    country = models.CharField( choices=COUNTRIES, max_length=5 )
    city = models.CharField( max_length=255 )
    area = models.CharField(max_length=255)
    zip_code =  models.CharField(max_length=5, blank=True, null=True)
    main_industry = models.IntegerField( choices=MAIN_INDUSTRY, default=1 )
    specific_industry = models.IntegerField( choices=SPECIFIC_INDUSTRY, default=1 )
    phone = models.CharField(max_length=255) 
    fax = models.CharField(max_length=255) 
    email = models.EmailField()
    url = models.URLField( verify_exists=True, blank=True, null=True )
    facebook = models.CharField( max_length=255, blank=True, null=True )
    twitter = models.CharField(max_length=255, blank=True, null=True )

    status = models.IntegerField( choices=COMPANY_STATUS, default=1 )
    is_active = models.BooleanField()
   
    directory = models.ManyToManyField( Directory, null=True, blank=True, through="ManyDirectoryCompany", symmetrical=False, related_name='in_directories' )
    company = models.ManyToManyField( "self" , null=True, blank=True, through="ManyCompanyCompany", symmetrical=False, related_name='related_company' )
    brand = models.ManyToManyField( Brand, null=True, blank=True ) #, through="ManyBrandCompany" )

    def __unicode__(self):
        return self.name


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



class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nationality = models.IntegerField( choices=COUNTRIES, default=1 )
    email = models.EmailField(max_length=75 )
    job_title = models.CharField(max_length=255)
    job_function = models.IntegerField( choices=PERSON_JOB_FUNCTION, default=1 )
    company = models.ManyToManyField( Company, through='ManyCompanyPerson')
    year = models.ManyToManyField( Year ) 

    def __unicode__(self):
        return "%s %s" % ( self.first_name , self.last_name )


#MANY TO MANY RELATIONS
#class ManyDirectoryCategory(models.Model):
#    directory = models.ForeignKey(Directory)
#    category = models.ForeignKey(Category)

class ManyCompanyPerson(models.Model):
    company = models.ForeignKey( Company )
    person = models.ForeignKey( Person )
    relation = models.IntegerField( choices=COMPANY_PERSON_RELATION, default=1 )

    def __unicode__(self):
        return mark_safe( "%s - %s" % ( self.company, self.person )  )


class ManyDirectoryCompany(models.Model):
    company = models.ForeignKey( Company )
    year = models.ForeignKey( Year ) 
    directory = models.ForeignKey(Directory)
    category = models.ForeignKey( Category, related_name="directory_company_category" )
    subcategory = models.ForeignKey( Category, related_name="directory_company_sub_category" )

#class ManyCompanyCategory(models.Model):
#    company = models.ForeignKey( Company )
#    category = models.ForeignKey(Category)
    
#class ManyCategoryPerson(models.Model):
#    category = models.ForeignKey(Category)
#    person = models.ForeignKey( Person )
#    relation = models.IntegerField( choices=CATEGORY_PERSON_RELATION, default=1 )
    

class ManyCompanyCompany(models.Model):
    child = models.ForeignKey( Company, null=True, blank=True, related_name='child' )
    parent = models.ForeignKey( Company, null=True, blank=True, related_name='parent' )
    relation = models.IntegerField( choices=COMPANY_COMPANY_RELATION, default=1 )
    
#class ManyBrandCompany(models.Model):
#    brand = models.ForeignKey( Brand )
#    company = models.ForeignKey( Company )
#    relation = models.IntegerField( choices=BRAND_COMPANY_RELATION, default=1 )

    
