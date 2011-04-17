from lib.halicea.HalRequestHandler import HalRequestHandler
from lib.Metropolis import MenuItem
from menu import menu
class MetropolisRequestHandler(HalRequestHandler):
    def render_dict(self, basedict):
        result = super(MetropolisRequestHandler, self).render_dict(basedict)
        if not result.has_key('menuLinks'):
            result['menuLinks'] = [MenuItem(link=m[0], title=m[1], isAdmin=m[2]) for m in menu]
        return result
    def __init__(self, *args, **kwargs):
        super(MetropolisRequestHandler, self).__init__(*args, **kwargs)