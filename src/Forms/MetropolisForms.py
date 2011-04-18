from lib.djangoFormImports import widgets, fields, extras
from google.appengine.ext.db.djangoforms import ModelForm
from Models.MetropolisModels import *
#{%block imports%}
#{%endblock%}
###############
class SelectMultiple(widgets.SelectMultiple):
    def value_from_datadict(self, data, files, name):
        try:
            return data.getall(name)
        except:
            return data.get(name, None)
class CheckboxSelectMultiple(widgets.CheckboxSelectMultiple):
    
    def value_from_datadict(data, name):
        try:
            return data.getall(name)
        except:
            return data.get(name, None)
class CompanyForm(ModelForm):
    class Meta():
        model=Company
        #exclude
##End Company

class ShopForm(ModelForm):
    WorkingDays = fields.MultipleChoiceField(widget=CheckboxSelectMultiple,choices=Days)
    class Meta():
        model=Shop
        exclude=['location_geocells']
##End Shop

class ProductForm(ModelForm):
    class Meta():
        model=Product
        #exclude
##End Product

class ShopProductForm(ModelForm):
    class Meta():
        model=ShopProduct
        exclude=['location_geocells']
##End ShopProduct

class ProfileForm(ModelForm):
    class Meta():
        model=Profile
        #exclude
##End Profile

class ShoppingCardForm(ModelForm):
    class Meta():
        model=ShoppingCard
        #exclude
##End ShoppingCard

class ShopingItemForm(ModelForm):
    class Meta():
        model=ShopingItem
        #exclude
##End ShopingItem

class PromotionForm(ModelForm):
    class Meta():
        model=Promotion
        #exclude
##End Promotion

class GrouperForm(ModelForm):
    class Meta():
        model=Grouper
        #exclude
##End Grouper
