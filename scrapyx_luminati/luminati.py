# -*- coding: utf-8 -*-
__author__ = 'Henry B. <tubnd.younet@gmail.com>'

from scrapy.exceptions import NotConfigured
import logging

log = logging.getLogger('scrapyx.luminati')

class LumninatiProxyMiddleware(object):
    def __init__(self, settings):
        if not settings.getbool('LUMINATI_ENABLED', True):
            raise NotConfigured

        self.proxy = settings.get('LUMINATI_URL', 'http://127.0.0.1:24000')

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings)
        return o

    def process_request(self, request, spider):
        if 'splash' in request.meta:
            request.meta['splash']['args']['proxy'] = self.proxy
        else:
            request.meta['proxy'] = self.proxy
