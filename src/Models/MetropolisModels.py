import settings
from google.appengine.ext import db
#{% block imports%}
from Models.BaseModels import Person
#{%endblock%}
################
class Company(db.Model):
    """TODO: Describe Company"""
    Name= db.StringProperty(required=True)
    ContactPhone= db.PhoneNumberProperty()
    ContactPerson= db.StringProperty()
    WebSite= db.LinkProperty()
    Address= db.TextProperty()
    DateAdded= db.DateProperty(auto_now_add=True)
    
    @classmethod
    def CreateNew(cls ,name,contactphone,contactperson,website,address, _isAutoInsert=False):
        result = cls(
                     Name=name,
                     ContactPhone=contactphone,
                     ContactPerson=contactperson,
                     WebSite=website,
                     Address=address,
                     )
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return self.Name 
## End Company


class Shop(db.Model):
    """TODO: Describe Shop"""
    Company = db.ReferenceProperty(reference_class=Company, collection_name="company_shops")
    Name= db.StringProperty(required=True, )
    Location= db.GeoPtProperty(required=True, )
    ContactPhone= db.PhoneNumberProperty()
    WorkingDays= db.StringListProperty(required=True, )
    NormalHoursStart= db.TimeProperty(required=True, default=8, )
    NormalHoursEnd= db.TimeProperty(required=True, default=20, )
    WeekendHoursStart= db.TimeProperty(required=True, default=10, )
    WeekendHoursEnd= db.TimeProperty(required=True, default=22, )
    IsWorkingOnWeekend= db.BooleanProperty(default=True, )
    IsWorkingSunday= db.BooleanProperty(default=False, )
    DateAdded= db.DateProperty(auto_now_add=True)
    DateModified = db.DateProperty(auto_now=True)
    
    @classmethod
    def CreateNew(cls ,name,location,contactphone,workingdays,normalhoursstart,normalhoursend,weekendhoursstart,weekendhoursend,isworkingonweekend,isworkingsunday , _isAutoInsert=False):
        result = cls(
                     Name=name,
                     Location=location,
                     ContactPhone=contactphone,
                     WorkingDays=workingdays,
                     NormalHoursStart=normalhoursstart,
                     NormalHoursEnd=normalhoursend,
                     WeekendHoursStart=weekendhoursstart,
                     WeekendHoursEnd=weekendhoursend,
                     IsWorkingOnWeekend=isworkingonweekend,
                     IsWorkingSunday=isworkingsunday,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return self.Name+"("+self.Company.Name+")"+str(self.Location) 
## End Shop


class Product(db.Model):
    """TODO: Describe Product"""
    Name= db.StringProperty(required=True, )
    Image= db.LinkProperty()
    IsFloat= db.BooleanProperty(default=False, )
    UnitName= db.StringProperty()
    DateAdded= db.DateProperty(auto_now_add=True)
    DateModified = db.DateProperty(auto_now=True)
    
    @classmethod
    def CreateNew(cls ,name,image,isfloat,unitname, _isAutoInsert=False):
        result = cls(
                     Name=name,
                     Image=image,
                     IsFloat=isfloat,
                     UnitName=unitname,
                     )
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        return self.Name 
## End Product

class ShopProduct(db.Model):
    """TODO: Describe ShopProduct"""
    ProductItem= db.ReferenceProperty(Product, collection_name='productitem_shopproducts', required=True, )
    Shop = db.ReferenceProperty(Shop,required=True, collection_name='shop_shopproducts')
    IsActive= db.BooleanProperty(default=True, )
    Name= db.StringProperty(required=True, )
    Image= db.LinkProperty()
    Price= db.FloatProperty()
    PriceCurrency= db.StringProperty()
    #Promotion
    IsPromotion= db.BooleanProperty()
    PromotionPrice= db.FloatProperty()
    #End Promotion
    #Grouper
    IsGrouper= db.BooleanProperty()
    GrouperPrice= db.FloatProperty()
    #End Promotion
    Count= db.FloatProperty()
    DateAdded= db.DateProperty(auto_now_add=True)
    DateModified = db.DateProperty(auto_now=True)
    
    @classmethod
    def CreateNew(cls ,productitem,isactive,name,image,price,pricecurrency,ispromotion,promotionprice,isgrouper,grouperprice,count , _isAutoInsert=False):
        result = cls(
                     ProductItem=productitem,
                     IsActive=isactive,
                     Name=name,
                     Image=image,
                     Price=price,
                     PriceCurrency=pricecurrency,
                     IsPromotion=ispromotion,
                     PromotionPrice=promotionprice,
                     IsGrouper=isgrouper,
                     GrouperPrice=grouperprice,
                     Count=count,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        return self.Name+' ('+str(self.Price)+' '+self.PriceCurrency+'/'+self.ProductItem.UnitName+')'
## End ShopProduct

class Profile(db.Model):
    """TODO: Describe UserProfile"""
    Person = db.ReferenceProperty(reference_class=Person, collection_name='person_profile')
    ProfileName = db.StringProperty(required=True)
    ProfilePicture= db.LinkProperty()
    CurrentLocation= db.GeoPtProperty()
    DateAdded= db.DateProperty(auto_now_add=True)
    DateModified = db.DateProperty(auto_now=True)
    @classmethod
    def CreateNew(cls, person, profilename, profilepicture, currentlocation, _isAutoInsert=False):
        result = cls(
                     Person=person,
                     ProfileName=profilename,
                     ProfilePicture=profilepicture,
                     CurrentLocation=currentlocation,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End UserProfile

class ShoppingCard(db.Model):
    """TODO: Describe ShoppingCard"""
    Total= db.FloatProperty()
    IsReal= db.BooleanProperty(default=False, )
    IsApproved= db.BooleanProperty(default=False, )
    DateCreated= db.DateProperty(auto_now_add=True)
    @classmethod
    def CreateNew(cls ,total,isreal,isapproved, _isAutoInsert=False):
        result = cls(
                     Total=total,
                     IsReal=isreal,
                     IsApproved=isapproved,
                     )
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End ShoppingCard


class ShopingItem(db.Model):
    """TODO: Describe ShopingItem"""
    Card= db.ReferenceProperty(ShoppingCard, collection_name='card_shopingitems', required=True, )
    Product= db.ReferenceProperty(Product, collection_name='product_shopingitems', required=True, )
    ShopFrom= db.ReferenceProperty(Shop, collection_name='shopfrom_shopingitems', )
    Price= db.FloatProperty(default=0, required=True)
    Currency = db.FloatProperty(required=True)
    Count= db.FloatProperty(default=1, required=True)
    
    @classmethod
    def CreateNew(cls ,card,product,shopfrom,price,currency, count , _isAutoInsert=False):
        result = cls(
                     Card=card,
                     Product=product,
                     ShopFrom=shopfrom,
                     Price=price,
                     Currency=currency,
                     Count=count,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        return str(self.Price)+str(self.Currency)+'x'+self.Count+'-'+self.Product.Name
## End ShopingItem


class Promotion(db.Model):
    """TODO: Describe Promotion"""
    Items= db.ListProperty(db.Key, required=True)
    Promotors = db.ListProperty(db.Key, required=True)
    IsCompanyWide = db.BooleanProperty(default=True)
    PromotionLink= db.LinkProperty()
    DateStart= db.DateProperty(required=True)
    DateEnd= db.DateProperty(required=True)
    
    @classmethod
    def CreateNew(cls ,items,promotionlink,datestart,dateend, isCompanyWide=True, promotors=None , _isAutoInsert=False):
        if not promotors:
            promotors = []
            if isCompanyWide:
                promotors = [items[0].Shop.Company.key(),]
            else:
                promotors = [items[0].Shop.key(),]
        result = cls(Items=items,
                     Promotors=promotors,
                     PromotionLink=promotionlink,
                     DateStart=datestart,
                     DateEnd=dateend,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return  ', '.join([x.Name for x in db.get(self.Items)])

## End Promotion

class Grouper(db.Model):
    """TODO: Describe Grouper"""
    Items= db.StringListProperty()
    PromotionLink= db.LinkProperty()
    CountsRequired= db.IntegerProperty()
    DateStart= db.DateProperty()
    DateEnd= db.DateProperty()
    
    @classmethod
    def CreateNew(cls ,items,promotionlink,countsrequired,datestart,dateend , _isAutoInsert=False):
        result = cls(
                     Items=items,
                     PromotionLink=promotionlink,
                     CountsRequired=countsrequired,
                     DateStart=datestart,
                     DateEnd=dateend,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End Grouper

