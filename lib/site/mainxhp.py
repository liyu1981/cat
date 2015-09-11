import tornado.web

class MainHandler(tornado.web.RequestHandler):

    @staticmethod
    def get_path():
        return r'/'

    def get(self):
        self.write("""
            <ul>
                <li><a href="/fb">Refresh Access Token</a></li>
                <li><a href="/getadsinsights">Get Ads Insights</a></li>
            </ul>
        """)
