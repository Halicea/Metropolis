import settings
from google.appengine.ext import db
#{% block imports%}
#{%endblock%}
################
class Company(db.Model):
    """TODO: Describe Company"""
    Name= db.StringProperty()
    ContactPhone= db.PhoneNumberProperty()
    ContactPerson= db.StringProperty()
    WebSite= db.LinkProperty()
    Address= db.TextProperty()
    DateAdded= db.DateProperty()
    
    @classmethod
    def CreateNew(cls ,name,contactphone,contactperson,website,address,dateadded , _isAutoInsert=False):
        result = cls(
                     Name=name,
                     ContactPhone=contactphone,
                     ContactPerson=contactperson,
                     WebSite=website,
                     Address=address,
                     DateAdded=dateadded,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End Company


class Shop(db.Model):
    """TODO: Describe Shop"""
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
    DateAdded= db.DateProperty()
    
    @classmethod
    def CreateNew(cls ,name,location,contactphone,workingdays,normalhoursstart,normalhoursend,weekendhoursstart,weekendhoursend,isworkingonweekend,isworkingsunday,dateadded , _isAutoInsert=False):
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
                     IsWorkingSunday=isworkingsunday,
                     DateAdded=dateadded,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End Shop


class Product(db.Model):
    """TODO: Describe Product"""
    Name= db.StringProperty(required=True, )
    Image= db.LinkProperty()
    IsFloat= db.BooleanProperty(default=False, )
    UnitName= db.StringProperty()
    DateAdded= db.DateProperty()
    
    @classmethod
    def CreateNew(cls ,name,image,isfloat,unitname,dateadded , _isAutoInsert=False):
        result = cls(
                     Name=name,
                     Image=image,
                     IsFloat=isfloat,
                     UnitName=unitname,
                     DateAdded=dateadded,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End Product


class ShopProduct(db.Model):
    """TODO: Describe ShopProduct"""
    ProductItem= db.ReferenceProperty(Product, collection_name='productitem_shopproducts', required=True, )
    IsActive= db.BooleanProperty(default=True, )
    Name= db.StringProperty(required=True, )
    Image= db.LinkProperty()
    Price= db.FloatProperty()
    PriceCurrency= db.StringProperty()
    IsPromotion= db.BooleanProperty()
    PromotionPrice= db.FloatProperty()
    IsGrouper= db.BooleanProperty()
    GrouperPrice= db.FloatProperty()
    Count= db.FloatProperty()
    
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
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End ShopProduct


class UserProfile(db.Model):
    """TODO: Describe UserProfile"""
    ProfilePicture= db.LinkProperty()
    CurrentLocation= db.GeoPtProperty()
    
    @classmethod
    def CreateNew(cls ,profilepicture,currentlocation , _isAutoInsert=False):
        result = cls(
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
    DateCreated= db.DateTimeProperty()
    
    @classmethod
    def CreateNew(cls ,total,isreal,isapproved,datecreated , _isAutoInsert=False):
        result = cls(
                     Total=total,
                     IsReal=isreal,
                     IsApproved=isapproved,
                     DateCreated=datecreated,)
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
    Price= db.FloatProperty(default=0, )
    Count= db.FloatProperty(default=1, )
    
    @classmethod
    def CreateNew(cls ,card,product,shopfrom,price,count , _isAutoInsert=False):
        result = cls(
                     Card=card,
                     Product=product,
                     ShopFrom=shopfrom,
                     Price=price,
                     Count=count,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
## End ShopingItem


class Promotion(db.Model):
    """TODO: Describe Promotion"""
    Items= db.StringListProperty()
    PromotionLink= db.LinkProperty()
    DateStart= db.DateProperty()
    DateEnd= db.DateProperty()
    
    @classmethod
    def CreateNew(cls ,items,promotionlink,datestart,dateend , _isAutoInsert=False):
        result = cls(
                     Items=items,
                     PromotionLink=promotionlink,
                     DateStart=datestart,
                     DateEnd=dateend,)
        if _isAutoInsert: result.put()
        return result
    def __str__(self):
        #TODO: Change the method to represent something meaningful
        return 'Change __str__ method' 
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

