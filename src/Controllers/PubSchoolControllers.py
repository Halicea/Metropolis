import os
import sys
import wsgiref.handlers

from django.utils import simplejson

from google.appengine.ext import db
from google.appengine.ext import webapp

from lib.geo import geotypes
from lib.Metropolis.MetropolisHandler import MetropolisRequestHandler as hrh
from Models.MetropolisModels import ShopProduct

def _merge_dicts(*args):
    """Merges dictionaries right to left. Has side effects for each argument."""
    return reduce(lambda d, s: d.update(s) or d, args)


class SearchService(webapp.RequestHandler):
    """Handler for public school search requests."""
    def get(self):
        def _simple_error(message, code=400):
            self.error(code)
            self.response.out.write(simplejson.dumps({
              'status': 'error',
              'error': { 'message': message },
              'results': []
            }))
            return None
          
        
        self.response.headers['Content-Type'] = 'application/json'
        center = geotypes.Point(float(self.request.get('lat')),
                                    float(self.request.get('lon')))
        max_results = 100
        if self.request.get('maxresults'):
            max_results = int(self.request.get('maxresults'))
        
        max_distance = 80000 # 80 km ~ 50 mi
        if self.request.get('maxdistance'):
            max_distance = float(self.request.get('maxdistance'))
        try:
            # Can't provide an ordering here in case inequality filters are used.
            base_query = ShopProduct.all()
            
            results = ShopProduct.proximity_fetch(
                                                   base_query,
                                                   center, max_results=max_results, max_distance=max_distance)
            results_obj = [
             {
                'lat': result.location.lat,
                'lng': result.location.lon,
             }
             for result in results]
        
            self.response.out.write(simplejson.dumps({
                
                'status': 'success',
                'results': results_obj
          }))
        except:
            return _simple_error(str(sys.exc_info()[1]), code=500)

class Search(hrh):
    def index(self, *args, **kwargs):
        self.SetTemplate(templateName='index.html')
        self.respond()
