#{%block imports%}
from Controllers import BaseControllers
from Controllers import StaticControllers
from Controllers import ShellControllers
from Controllers import MetropolisControllers
from Controllers import PubSchoolControllers
#{%endblock%}

webapphandlers = [
#{%block ApplicationControllers %}
#('/', BaseControllers.LoginController),
#{% block BaseControllers %}
('/Login', BaseControllers.LoginController),
('/Logout',BaseControllers.LogoutController),
('/AddUser', BaseControllers.AddUserController),
('/WishList', BaseControllers.WishListController),
('/admin/Role', BaseControllers.RoleController),
('/admin/RoleAssociation', BaseControllers.RoleAssociationController),
('/Base/WishList', BaseControllers.WishListController),
#{%endblock%}

#{%block StaticControllers%}
('/NotAuthorized', StaticControllers.NotAuthorizedController),
#{%endblock%}


#{%block ShellControllers%}
('/admin/Shell', ShellControllers.FrontPageController),
('/admin/stat.do', ShellControllers.StatementController),
#{%endblock%}

#{%block MetropolisControllers%}
('/', MetropolisControllers.ObjectTypes),
('/ss', PubSchoolControllers.SearchService),
('/Metropolis/Company', MetropolisControllers.CompanyController),
('/Metropolis/Shop', MetropolisControllers.ShopController),
('/Metropolis/Product', MetropolisControllers.ProductController),
(r'/Metropolis/Product/Search/(.*)', MetropolisControllers.ProductSearchController),
(r'/Metropolis/Product/Search', MetropolisControllers.ProductSearchController),
('/Metropolis/Category/(.*)', MetropolisControllers.ProductCategoryController),
('/Metropolis/ShopProduct', MetropolisControllers.ShopProductController),
('/Metropolis/UserProfile', MetropolisControllers.ProfileController),
('/Metropolis/ShoppingCard', MetropolisControllers.ShoppingCardController),
('/Metropolis/ShopingItem', MetropolisControllers.ShopingItemController),
('/Metropolis/Promotion', MetropolisControllers.PromotionController),
('/Metropolis/Grouper', MetropolisControllers.GrouperController),
#{%endblock%}
#{%endblock%}
('/(.*)', StaticControllers.NotExistsController),
]

