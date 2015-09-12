import tornado .web 
import tornado .auth 

from urlparse import urljoin 

from cat .xhpy .pylib import *
from cat import conf 

class FacebookAccessTokenHandler (tornado .web .RequestHandler ,tornado .auth .FacebookGraphMixin ):

    @staticmethod 
    def get_path ():
        return '/fb'

    @tornado .gen .coroutine 
    def get (self ):
        url =("%s://%s%s"%(self .request .protocol ,self .request .host ,self .request .uri ))
        c =conf .get ('fb')
        l =conf .get ('live')
        if self .get_argument ("code",False ):
            user =yield self .get_authenticated_user (redirect_uri =urljoin (url ,self .get_path ()),client_id =c ["FACEBOOK_APP_ID"],client_secret =c ["FACEBOOK_APP_SECRET"],code =self .get_argument ("code"))

            conf .set ('access_token',user ["access_token"])
            self .write (str (xhpy_p ({},['Done with:',l ["access_token"],', saved in live_obj!',])))
        else :
            yield self .authorize_redirect (redirect_uri =urljoin (url ,self .get_path ()),client_id =c ["FACEBOOK_APP_ID"],extra_params ={"scope":"ads_management,ads_read"})
