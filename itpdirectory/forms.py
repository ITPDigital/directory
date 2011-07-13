from django import forms
from itpdirectory.models import Category

class CategoryForm(Forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(VoucherForm, self).__init__(*args, **kwargs)
        #self.fields['used_outlet'].choices = [(outlet.id, outlet) for outlet in outlets]
        print self.fields

    class Meta:
        model = Category


