import tornado .web 
from cat .xhpy .pylib import *

class MainHandler (tornado .web .RequestHandler ):

    @staticmethod 
    def get_path ():
        return r'/'

    def get (self ):
        self .write (str (xhpy_ul ({},[xhpy_li ({},[xhpy_a ({'href':"/fb",},['Refresh Access Token',]),]),xhpy_li ({},[xhpy_a ({'href':"/getadsinsights",},['Get Ads Insights',]),]),])))
