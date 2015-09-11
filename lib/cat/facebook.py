import logging

from facebookads import FacebookAdsApi
from facebookads import FacebookSession

import .conf

_ok = False

def ok():
    global _ok
    if not _ok:
        c = conf.get('fb')
        l = conf.get('live')
        if "FACEBOOK_APP_ID" in c and \
           "FACEBOOK_APP_SECRET" in c and \
           "access_token" in l:
            session = FacebookSession(
                c['FACEBOOK_APP_ID'],
                c['FACEBOOK_APP_SECRET'],
                l['access_token'],
            )
            api = FacebookAdsApi(session)
            FacebookAdsApi.set_default_api(api)
            logging.info(
               'facebook marketing api inited: id={}'.format(
                    c['FACEBOOK_APP_ID']
                )
            )
            _ok = True
    return _ok