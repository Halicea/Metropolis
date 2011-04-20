import settings
#from lib.halicea.HalRequestHandler import HalRequestHandler as hrh
from lib.Metropolis.MetropolisHandler import MetropolisRequestHandler as hrh
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
from Models.MetropolisModels import Profile
from Forms.MetropolisForms import ProfileForm
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
class ObjectTypes(hrh):
    def SetOperations(self):
        self.operations = {'default':{'method':self.default}}
    def default(self, *args, **kwargs):
        from handlerMap import webapphandlers as wah
        a = """<html><head><title>Test</title></head>
        <body>
            {{items}}
        </body></html>"""
        links = ["<a href='"+x[0]+"'>"+x[0]+'</a>' for x in wah if x[0].startswith('/Metropolis')]
        self.respond_static(a.replace("{{items}}", '<br/>'.join(links)))

class MetropolisHandlers(hrh):
    def SetOperations(self):
        self.operations = {'default':{'method':self.show}}
    def show(self, *args, **kwargs):
        from handlerMap import webapphandlers as wah
        response = "<html><title></title><body>{{items}}</body></html>"
        self.respond_static(response.replace("{{items}}", '<br/>'.join(["<a href='"+x[0]+"'>"+x[0]+"</a>" for x in wah])))
class CompanyController(hrh):
#    def SetOperations(self):
#        self.operations.update({'search':{'method':self.search}})
    def search(self, *args):
        if self.params.search:
            pass
            
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
            self.SetTemplate(templateName = 'Company_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'CompanyForm': form}

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
            return {'op':'insert' ,'CompanyForm':CompanyForm()}

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
            self.SetTemplate(templateName = 'Shop_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'ShopForm': form}

    def edit(self, *args):
        if self.params.key:
            item = Shop.get(self.params.key)
            if item:
                return {'op':'update', 'ShopForm': ShopForm(instance=item)}
            else:
                self.status = 'Shop does not exists'
                self.redirect(ShopController.get_url())
        else:
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
                return {'Shop': item }
            else:
                self.status = 'Shop does not exists'
                self.redirect(ShopController.get_url())
        else:
            self.redirect(ShopController.get_url())

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
            self.SetTemplate(templateName = 'Product_edit.html')
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
                return {'op':'update', 'Product': item}
            else:
                self.status = 'Product does not exists'
                self.redirect(ProductController.get_url())
        else:
            self.status = 'Key not provided'
            self.redirect(ProductController.get_url())

class ProductSearchController(hrh):
    def SetOperations(self):
        self.operations = {'default':{'method':'search'}}
    def search(self, searchCondition=None, *args, **kwargs):
        self.SetTemplate(templateName='index.html')
        mySearch = urllib.unquote(searchCondition or self.params.searchCondition)
        if mySearch:
            self.respond({'results':Product.all().fetch(limit=1000, offset=0)})
        else:
            self.status= "No Condition given, so no results displayed!"
            self.respond()
class ProductCategoryController(hrh):
    def SetOperations(self):
        self.operations = {'default':{'method':'search'}}
    def search(self, searchItem,  *args, **kwargs):
        self.SetTemplate(templateName="Product_index.html")
        return {"ProductList":Product.gql("WHERE Categories = :s", s=searchItem).fetch(limit=100, offset=0)}
    
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
            self.SetTemplate(templateName = 'ShopProduct_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'ShopProductForm': form}

    def edit(self, *args):
        if self.params.key:
            item = ShopProduct.get(self.params.key)
            if item:
                return {'op':'update', 'ShopProductForm': ShopProductForm(instance=item)}
            else:
                self.status = 'ShopProduct does not exists'
                self.redirect(ShopProductController.get_url())
        else:
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
                return {'op':'update', 'ShopProductForm': ShopProductForm(instance=item)}
            else:
                self.status = 'ShopProduct does not exists'
                self.redirect(ShopProductController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShopProductForm':ShopProductForm()}

class ProfileController(hrh):
    
    def delete(self,*args):    
        if args[1]:
            item = Profile.gql("WHERE ProfileName= :p", p=args[1]).get()
            if item:
                item.delete()
                self.status ='Profile is deleted!'
            else:
                self.status='Profile does not exist'
        else:
            self.status = 'Key was not Provided!'
        self.redirect(ProfileController.get_url())

    def save(self, *args):
        instance = None
        if args[1]:
            instance = Profile.gql("WHERE ProfileName = :p", p=args[1]).get()
        form=ProfileForm(data=self.request.POST, instance=instance)
        if form.is_valid():
            result=form.save(commit=False)
            result.put()
            self.status = 'Profile is saved'
            self.redirect(ProfileController.get_url(result.ProfileName))
        else:
            self.SetTemplate(templateName = 'Profile_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'ProfileForm': form}

    def edit(self, *args):
        if len(args)>1 and args[1]:
            item = Profile.gql("WHERE ProfileName = :p", p=args[1]).get()
            if item:
                return {'op':'update', 'ProfileForm': ProfileForm(instance=item)}
            else:
                self.status = 'Profile does not exists'
                self.redirect(ProfileController.get_url(args[1]))
        else:
            return {'op':'insert' ,'ProfileForm':ProfileForm()}

    def index(self, *args):
        self.SetTemplate(templateName="Profile_index.html")
        results =None
        index = 0; count=20
        try:
            index = int(self.params.index)
            count = int(self.params.count)
        except:
            pass
        nextIndex = index+count;
        previousIndex = index<=0 and -1 or (index-count>0 and 0 or index-count) 
        result = {'ProfileList': Profile.all().fetch(limit=count, offset=index)}
        result.update(locals())
        return result

    def details(self, *args):
        if len(args) and args[1]:
            item = Profile.gql("WHERE ProfileName = :p", p=args[1]).get()
            if item:
                return {'op':'update', 'ProfileForm': ProfileForm(instance=item)}
            else:
                self.status = 'Profile does not exists'
                self.redirect(ProfileController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ProfileForm':ProfileForm()}

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
            self.SetTemplate(templateName = 'ShoppingCard_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'ShoppingCardForm': form}

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
                return {'op':'update', 'ShoppingCardForm': ShoppingCardForm(instance=item)}
            else:
                self.status = 'ShoppingCard does not exists'
                self.redirect(ShoppingCardController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShoppingCardForm':ShoppingCardForm()}

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
            self.SetTemplate(templateName = 'ShopingItem_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'ShopingItemForm': form}

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
                return {'op':'update', 'ShopingItemForm': ShopingItemForm(instance=item)}
            else:
                self.status = 'ShopingItem does not exists'
                self.redirect(ShopingItemController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'ShopingItemForm':ShopingItemForm()}

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
            self.SetTemplate(templateName = 'Promotion_edit.html')
            self.status = 'Form is not Valid'
            return {'op':'update', 'PromotionForm': form}

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
                return {'op':'update', 'PromotionForm': PromotionForm(instance=item)}
            else:
                self.status = 'Promotion does not exists'
                self.redirect(PromotionController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'PromotionForm':PromotionForm()}

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
            self.SetTemplate(templateName = 'Grouper_edit.html')
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
                return {'op':'update', 'GrouperForm': GrouperForm(instance=item)}
            else:
                self.status = 'Grouper does not exists'
                self.redirect(GrouperController.get_url())
        else:
            self.status = 'Key not provided'
            return {'op':'insert' ,'GrouperForm':GrouperForm()}
