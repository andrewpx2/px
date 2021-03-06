#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os
import chucknorris
import pxyahoo
import catimage
import pxbun
import pxfunpic
import pxgiffun
import pxgiphy
import pxyom
import pxeliz
import yodapx
import pxdad
import pxdog
import lovepx
import pxinsult
import pxmeme

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    
    if req.get("result").get("action") == "chuckjoke":
        res = chucknorris.processRequest(req)
    elif req.get("result").get("action") == "yahooWeatherForecast":
        res = pxyahoo.processRequest(req)
    elif req.get("result").get("action") == "meow":
        res = catimage.processRequest(req)
    elif req.get("result").get("action") == "bunny":
        res = pxbun.processRequest(req)
    elif req.get("result").get("action") == "funpic":
        res = pxfunpic.processRequest(req)
    elif req.get("result").get("action") == "giffun":
        res = pxgiffun.processRequest(req)
    elif req.get("result").get("action") == "giphypx":
        res = pxgiphy.processRequest(req)
    elif req.get("result").get("action") == "yom":
        res = pxyom.processRequest(req)
    elif req.get("result").get("action") == "elizpx":
        res = pxeliz.processRequest(req)
    elif req.get("result").get("action") == "pxyoda":
        res = yodapx.processRequest(req)
    elif req.get("result").get("action") == "dadpx":
        res = pxdad.processRequest(req)
    elif req.get("result").get("action") == "dogpx":
        res = pxdog.processRequest(req)
    elif req.get("result").get("action") == "pxluv":
        res = lovepx.processRequest(req)
    elif req.get("result").get("action") == "insultpx":
        res = pxinsult.processRequest(req)
    elif req.get("result").get("action") == "memepx":
        res = pxmeme.processRequest(req)
    else:
        return{}
    
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
