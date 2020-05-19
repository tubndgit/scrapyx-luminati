# scrapy-luminati

Luminati middleware for Scrapy (http://scrapy.org/)

Required
--------

    python version >= 2.7


Install
--------

Checkout the source and run

    python setup.py install


settings.py
-----------

    # Activate the middleware
    LUMINATI_ENABLED = True
    
    # The API key 
    LUMINATI_URL = 'http://127.0.0.1:24000'

    DOWNLOADER_MIDDLEWARES = {
        'scrapyx_luminati.LumninatiProxyMiddleware': 610,
    }
