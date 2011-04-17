#{%block imports%}
from Controllers import BaseControllers
from Controllers import StaticControllers
from Controllers import ShellControllers
from Controllers import MetropolisControllers
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
('/Contact', StaticControllers.ContactController),
('/About', StaticControllers.AboutController),
('/Links', StaticControllers.LinksController),
('/NotAuthorized', StaticControllers.NotAuthorizedController),
#{%endblock%}


#{%block ShellControllers%}
('/admin/Shell', ShellControllers.FrontPageController),
('/admin/stat.do', ShellControllers.StatementController),
#{%endblock%}

#{%block MetropolisControllers%}
('/', MetropolisControllers.MetropolisHandlers),
('/Metropolis', MetropolisControllers.MetropolisHandlers),
('/Metropolis/Company', MetropolisControllers.CompanyController),
('/Metropolis/Shop', MetropolisControllers.ShopController),
('/Metropolis/Product', MetropolisControllers.ProductController),
('/Metropolis/Product/Search/(.*)', MetropolisControllers.ProductSearchController),
('/Metropolis/ShopProduct', MetropolisControllers.ShopProductController),
('/Metropolis/Profile/(.*)', MetropolisControllers.ProfileController),
('/Metropolis/ShoppingCard', MetropolisControllers.ShoppingCardController),
('/Metropolis/ShopingItem', MetropolisControllers.ShopingItemController),
('/Metropolis/Promotion', MetropolisControllers.PromotionController),
('/Metropolis/Grouper', MetropolisControllers.GrouperController),
#{%endblock%}
#{%endblock%}
('/(.*)', StaticControllers.NotExistsController),
]

