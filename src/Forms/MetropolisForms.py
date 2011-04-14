from lib.djangoFormImports import widgets, fields, extras
from google.appengine.ext.db.djangoforms import ModelForm
from Models.MetropolisModels import *
#{%block imports%}
#{%endblock%}
###############

class CompanyForm(ModelForm):
    class Meta():
        model=Company
        #exclude
##End Company

class ShopForm(ModelForm):
    class Meta():
        model=Shop
        #exclude
##End Shop

class ProductForm(ModelForm):
    class Meta():
        model=Product
        #exclude
##End Product

class ShopProductForm(ModelForm):
    class Meta():
        model=ShopProduct
        #exclude
##End ShopProduct

class UserProfileForm(ModelForm):
    class Meta():
        model=UserProfile
        #exclude
##End UserProfile

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
