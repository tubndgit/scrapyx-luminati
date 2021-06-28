# scrapyx-luminati

[Luminati](https://brightdata.grsm.io/p302843) middleware for [Scrapy](http://scrapy.org/)

Required
--------

    python version >= 2.7


Install
--------

Checkout the source and run

    python setup.py install

Or

    pip install scrapyx-luminati


settings.py
-----------

    # Activate the middleware
    LUMINATI_ENABLED = True
    
    # The Luminati URL
    LUMINATI_URL = 'http://127.0.0.1:24000'

    DOWNLOADER_MIDDLEWARES = {
        'scrapyx_luminati.LumninatiProxyMiddleware': 610,
    }
