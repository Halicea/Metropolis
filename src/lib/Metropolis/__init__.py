class MenuItem(object):
    def __init__(self, link, title, isAdmin=False):
        self.Link=link
        self.Title=title
        self.AdminOnly=isAdmin
    def render(self, attrs={}):
        str = '<a href=\"%s\" %s >%s</a>'%self.Link, ' '.join([k+'='+v for k,v in attrs.iteritems()]), self.Title
