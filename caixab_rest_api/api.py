#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Caixa transactions REST API testing script.

import requests

requests.packages.urllib3.disable_warnings()

def get_token(auth_endpoint, api_keys, api_secret):
      """
      Get an authorization token.
      """
      data = {
        'grant_type': 'api_credentials',
        'client_id': api_keys,
        'client_secret': api_secret
      }
      res = requests.post(auth_endpoint, data=data)
      if res.status_code == 200:
        token = res.json()['access_token']
        return token
      else:
        raise Exception('An error occurred: %s.' % (res.status_code))

class api_request(object):

    def __init__(self, api_key, api_secret, server):
        """
        api_request main function.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.server = server
        self.headers = {
            'Authorization': get_token('%s/oauth2/token', api_key, api_secret)
        }

    def make_request(self, method, endpoint, data = None):
        """
        API request function.
        """
        url = '%s%s' % (self.server, endpoint)
        if data is not None:
            self.headers['Content-Type'] = 'application/json'
        if method == 'GET':
            res = requests.get(url, headers=self.headers)
        if method == 'POST':
            res = requests.post(url, data=data, headers=self.headers)
        if method == 'PUT':
            res = requests.put(url, data=data, headers=self.headers)
        if method == 'DELETE':
            res = requests.put(url, data=data, headers=self.headers)
        if res.status_code in [200, 201]:
            return res.json()
        else:
            raise Exception('An error ocurrend: %s - %s' % (res.status_code, res.json()))