# -*- coding: utf-8 -*-
import os 
import settings 
os.environ['DJANGO_SETTINGS_MODULE']  = 'settings'
#from google.appengine.dist import use_library
#use_library('django', '1.2')
from SvcHandlerMap import webapphandlers
from lib.webapp2 import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from lib.gaesessions import SessionMiddleware
from django.conf import settings as sett
#sett.configure(TEMPLATE_DIRS=settings.TEMPLATE_DIRS)

template.register_template_library(
    'django.contrib.humanize.templatetags.humanize')
template.register_template_library('lib.halicea.templatelib')

application = webapp.WSGIApplication(webapphandlers, debug=settings.DEBUG)

COOKIE_KEY = '''2zÆœ;¾±þ”¡j:ÁõkçŸÐ÷8{»Ën¿A—jÎžQAQqõ"bøó÷*%†™ù¹b¦$vš¡¾4ÇŸ^ñ5¦'''
def webapp_add_wsgi_middleware(app):
#    from google.appengine.ext.appstats import recording
    app = SessionMiddleware(app, cookie_key=COOKIE_KEY)
#    app = recording.appstats_wsgi_middleware(app)
    return app
def main():
    run_wsgi_app(webapp_add_wsgi_middleware(application))

if __name__ == "__main__":
    main()
