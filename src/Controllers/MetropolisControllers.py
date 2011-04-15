import settings
from lib.halicea.HalRequestHandler import HalRequestHandler as hrh
from lib.halicea.decorators import *
from google.appengine.ext import db
import urllib
#{%block imports%}
from Models.MetropolisModels import Company
from Forms.MetropolisForms import CompanyForm
from Models.MetropolisModels import Shop
from Forms.MetropolisForms import ShopForm
from Models.MetropolisModels import Product
from Forms.MetropolisForms import ProductForm
from Models.MetropolisModels import ShopProduct
from Forms.MetropolisForms import ShopProductForm
from Models.MetropolisModels import UserProfile
from Forms.MetropolisForms import UserProfileForm
from Models.MetropolisModels import ShoppingCard
from Forms.MetropolisForms import ShoppingCardForm
from Models.MetropolisModels import ShopingItem
from Forms.MetropolisForms import ShopingItemForm
from Models.MetropolisModels import Promotion
from Forms.MetropolisForms import PromotionForm
from Models.MetropolisModels import Grouper
from Forms.MetropolisForms import GrouperForm
#{%endblock%}
################################

class CompanyController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = Company.get(self.params.key)
            if item:
                item.delete()
                self.status ='Company is deleted!'
            else:
                self.status='Company does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(CompanyController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = Company.get(self.params.key)
        form=CompanyForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'Company is saved'
            self.redirect(CompanyController.get_url())
        else:
            self.SetTemplate(templateName = 'Company_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'CompanyForm': form}

    def edit(self, *args):
        if self.params.key:
            item = Company.get(self.params.key)
            if item:
                return {'op':'update', 'CompanyForm': CompanyForm(instance=item)}
            else:
                self.status = 'Company does not exists'
                self.redirect(CompanyController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'CompanyForm':CompanyForm()}

    def index(self, *args):
        self.SetTemplate(templateName="Company_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'CompanyList': Company.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = Company.get(self.params.key)
            if item:
                return {'op':'upd', 'CompanyForm': CompanyForm(instance=item)}
            else:
                self.status = 'Company does not exists'
                self.redirect(CompanyController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'CompanyForm':CompanyForm()}

class ShopController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = Shop.get(self.params.key)
            if item:
                item.delete()
                self.status ='Shop is deleted!'
            else:
                self.status='Shop does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(ShopController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = Shop.get(self.params.key)
        form=ShopForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'Shop is saved'
            self.redirect(ShopController.get_url())
        else:
            self.SetTemplate(templateName = 'Shop_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'ShopForm': form}

    def edit(self, *args):
        if self.params.key:
            item = Shop.get(self.params.key)
            if item:
                return {'op':'update', 'ShopForm': ShopForm(instance=item)}
            else:
                self.status = 'Shop does not exists'
                self.redirect(ShopController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShopForm':ShopForm()}

    def index(self, *args):
        self.SetTemplate(templateName="Shop_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'ShopList': Shop.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = Shop.get(self.params.key)
            if item:
                return {'op':'upd', 'ShopForm': ShopForm(instance=item)}
            else:
                self.status = 'Shop does not exists'
                self.redirect(ShopController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'ShopForm':ShopForm()}

class ProductController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = Product.get(self.params.key)
            if item:
                item.delete()
                self.status ='Product is deleted!'
            else:
                self.status='Product does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(ProductController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = Product.get(self.params.key)
        form=ProductForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'Product is saved'
            self.redirect(ProductController.get_url())
        else:
            self.SetTemplate(templateName = 'Product_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'ProductForm': form}

    def edit(self, *args):
        if self.params.key:
            item = Product.get(self.params.key)
            if item:
                return {'op':'update', 'ProductForm': ProductForm(instance=item)}
            else:
                self.status = 'Product does not exists'
                self.redirect(ProductController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ProductForm':ProductForm()}

    def index(self, *args):
        self.SetTemplate(templateName="Product_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'ProductList': Product.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = Product.get(self.params.key)
            if item:
                return {'op':'upd', 'ProductForm': ProductForm(instance=item)}
            else:
                self.status = 'Product does not exists'
                self.redirect(ProductController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'ProductForm':ProductForm()}

class ProductSearchController(hrh):
    def SetOperations(self):
        self.operations = {'default':{'method':'search'}}
    def search(self, searchCondition=None, *args, **kwargs):
        mySearch = urllib.unquote(searchCondition or self.params.searchCondition)
        if mySearch:
            return Product.all().fetch(limit=1000, offset=0) or "No product found for <b>%s</b> search!"%mySearch
        else:
            return "No Condition given, so no results displayed!"+ str(args)
        
class ShopProductController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = ShopProduct.get(self.params.key)
            if item:
                item.delete()
                self.status ='ShopProduct is deleted!'
            else:
                self.status='ShopProduct does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(ShopProductController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = ShopProduct.get(self.params.key)
        form=ShopProductForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'ShopProduct is saved'
            self.redirect(ShopProductController.get_url())
        else:
            self.SetTemplate(templateName = 'ShopProduct_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'ShopProductForm': form}

    def edit(self, *args):
        if self.params.key:
            item = ShopProduct.get(self.params.key)
            if item:
                return {'op':'update', 'ShopProductForm': ShopProductForm(instance=item)}
            else:
                self.status = 'ShopProduct does not exists'
                self.redirect(ShopProductController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShopProductForm':ShopProductForm()}

    def index(self, *args):
        self.SetTemplate(templateName="ShopProduct_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'ShopProductList': ShopProduct.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = ShopProduct.get(self.params.key)
            if item:
                return {'op':'upd', 'ShopProductForm': ShopProductForm(instance=item)}
            else:
                self.status = 'ShopProduct does not exists'
                self.redirect(ShopProductController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'ShopProductForm':ShopProductForm()}

class UserProfileController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = UserProfile.get(self.params.key)
            if item:
                item.delete()
                self.status ='UserProfile is deleted!'
            else:
                self.status='UserProfile does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(UserProfileController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = UserProfile.get(self.params.key)
        form=UserProfileForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'UserProfile is saved'
            self.redirect(UserProfileController.get_url())
        else:
            self.SetTemplate(templateName = 'UserProfile_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'UserProfileForm': form}

    def edit(self, *args):
        if self.params.key:
            item = UserProfile.get(self.params.key)
            if item:
                return {'op':'update', 'UserProfileForm': UserProfileForm(instance=item)}
            else:
                self.status = 'UserProfile does not exists'
                self.redirect(UserProfileController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'UserProfileForm':UserProfileForm()}

    def index(self, *args):
        self.SetTemplate(templateName="UserProfile_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'UserProfileList': UserProfile.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = UserProfile.get(self.params.key)
            if item:
                return {'op':'upd', 'UserProfileForm': UserProfileForm(instance=item)}
            else:
                self.status = 'UserProfile does not exists'
                self.redirect(UserProfileController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'UserProfileForm':UserProfileForm()}

class ShoppingCardController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = ShoppingCard.get(self.params.key)
            if item:
                item.delete()
                self.status ='ShoppingCard is deleted!'
            else:
                self.status='ShoppingCard does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(ShoppingCardController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = ShoppingCard.get(self.params.key)
        form=ShoppingCardForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'ShoppingCard is saved'
            self.redirect(ShoppingCardController.get_url())
        else:
            self.SetTemplate(templateName = 'ShoppingCard_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'ShoppingCardForm': form}

    def edit(self, *args):
        if self.params.key:
            item = ShoppingCard.get(self.params.key)
            if item:
                return {'op':'update', 'ShoppingCardForm': ShoppingCardForm(instance=item)}
            else:
                self.status = 'ShoppingCard does not exists'
                self.redirect(ShoppingCardController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShoppingCardForm':ShoppingCardForm()}

    def index(self, *args):
        self.SetTemplate(templateName="ShoppingCard_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'ShoppingCardList': ShoppingCard.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = ShoppingCard.get(self.params.key)
            if item:
                return {'op':'upd', 'ShoppingCardForm': ShoppingCardForm(instance=item)}
            else:
                self.status = 'ShoppingCard does not exists'
                self.redirect(ShoppingCardController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'ShoppingCardForm':ShoppingCardForm()}

class ShopingItemController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = ShopingItem.get(self.params.key)
            if item:
                item.delete()
                self.status ='ShopingItem is deleted!'
            else:
                self.status='ShopingItem does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(ShopingItemController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = ShopingItem.get(self.params.key)
        form=ShopingItemForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'ShopingItem is saved'
            self.redirect(ShopingItemController.get_url())
        else:
            self.SetTemplate(templateName = 'ShopingItem_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'ShopingItemForm': form}

    def edit(self, *args):
        if self.params.key:
            item = ShopingItem.get(self.params.key)
            if item:
                return {'op':'update', 'ShopingItemForm': ShopingItemForm(instance=item)}
            else:
                self.status = 'ShopingItem does not exists'
                self.redirect(ShopingItemController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShopingItemForm':ShopingItemForm()}

    def index(self, *args):
        self.SetTemplate(templateName="ShopingItem_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'ShopingItemList': ShopingItem.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = ShopingItem.get(self.params.key)
            if item:
                return {'op':'upd', 'ShopingItemForm': ShopingItemForm(instance=item)}
            else:
                self.status = 'ShopingItem does not exists'
                self.redirect(ShopingItemController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'ShopingItemForm':ShopingItemForm()}

class PromotionController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = Promotion.get(self.params.key)
            if item:
                item.delete()
                self.status ='Promotion is deleted!'
            else:
                self.status='Promotion does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(PromotionController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = Promotion.get(self.params.key)
        form=PromotionForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'Promotion is saved'
            self.redirect(PromotionController.get_url())
        else:
            self.SetTemplate(templateName = 'Promotion_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'PromotionForm': form}

    def edit(self, *args):
        if self.params.key:
            item = Promotion.get(self.params.key)
            if item:
                return {'op':'update', 'PromotionForm': PromotionForm(instance=item)}
            else:
                self.status = 'Promotion does not exists'
                self.redirect(PromotionController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'PromotionForm':PromotionForm()}

    def index(self, *args):
        self.SetTemplate(templateName="Promotion_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'PromotionList': Promotion.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = Promotion.get(self.params.key)
            if item:
                return {'op':'upd', 'PromotionForm': PromotionForm(instance=item)}
            else:
                self.status = 'Promotion does not exists'
                self.redirect(PromotionController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'PromotionForm':PromotionForm()}

class GrouperController(hrh):
    
    def delete(self,*args):
        if self.params.key:
            item = Grouper.get(self.params.key)
            if item:
                item.delete()
                self.status ='Grouper is deleted!'
            else:
                self.status='Grouper does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(GrouperController.get_url())

    def save(self, *args):
        instance = None
        if self.params.key:
            instance = Grouper.get(self.params.key)
        form=GrouperForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'Grouper is saved'
            self.redirect(GrouperController.get_url())
        else:
            self.SetTemplate(templateName = 'Grouper_shw.html')
            self.status = 'Form is not Valid'
            return {'op':'upd', 'GrouperForm': form}

    def edit(self, *args):
        if self.params.key:
            item = Grouper.get(self.params.key)
            if item:
                return {'op':'update', 'GrouperForm': GrouperForm(instance=item)}
            else:
                self.status = 'Grouper does not exists'
                self.redirect(GrouperController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'GrouperForm':GrouperForm()}

    def index(self, *args):
        self.SetTemplate(templateName="Grouper_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'GrouperList': Grouper.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if self.params.key:
            item = Grouper.get(self.params.key)
            if item:
                return {'op':'upd', 'GrouperForm': GrouperForm(instance=item)}
            else:
                self.status = 'Grouper does not exists'
                self.redirect(GrouperController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'ins' ,'GrouperForm':GrouperForm()}
