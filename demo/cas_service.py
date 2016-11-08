#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
"""
__author__ = xyy
__mtime__ = 2016/11/2
"""
import urllib
from xml.etree import ElementTree


class CasService:
    @staticmethod
    def _get_service_url(request):
        settings = request.registry.settings
        cas_url = settings.get('cas_server_url')
        brms_url = settings.get('brms_url')
        return cas_url, brms_url

    def logout_url(self, request):
        urls = self._get_service_url(request)
        url = urllib.parse.urljoin(urls[0], 'logout?service=%s' % urls[0]) + 'login?service=%s' % urls[1] + 'login'
        return url

    def verify_proxy_ticket(self, request, ticket):
        """Verifies CAS 2.0+ XML-based authentication ticket.
        Returns username on success and None on failure.
        """
        settings = request.registry.settings
        brms_url = str(settings.get('brms_url')) + 'login'
        params = {'ticket': ticket, 'service': brms_url}
        cas_server = settings.get('cas_server_url')
        # url = (urllib.parse.urljoin(cas_server, 'serviceValidate') + '?' + urllib.parse.urlencode(params))
        url = (urllib.parse.urljoin(cas_server, 'proxyValidate') + '?' + urllib.parse.urlencode(params))
        page = urllib.request.urlopen(url)
        try:
            response = page.read()
            tree = ElementTree.fromstring(response)
            # if tree[0].tag.endswith('authenticationSuccess'):
            #     username = tree[0][0].text
            #     proxies = []
            #     if len(tree[0]) > 1:
            #         for element in tree[0][1]:
            #             proxies.append(element.text)
            #     return {"username": username, "proxies": proxies}
            # else:
            #     return None
            if tree[0].tag.endswith('authenticationSuccess'):
                return tree[0][0].text
            else:
                return None
        finally:
            page.close()

