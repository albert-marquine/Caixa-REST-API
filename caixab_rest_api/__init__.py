#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Caixa transactions REST API testing script.

def run(arguments):
    """
    
    """
    from caixab.api import api_request
    api = api_request(arguments.api_key, arguments.api_secret, 'https://18.101.17.111/api/')
    response = api.make_request(arguments.action, arguments.endpoint, arguments.data)
    print(response)


def make_parser():
    """
    Input string parser
    """
    import argparse
    parser = argparse.ArgumentParser(description="Caixa's transactions API library.")
    parser.add_argument('-api_key','-api_key', help=' Enter your api key.', required=True)
    parser.add_argument('-secret_key','-secret_key', help=' Enter your api key.', required=True)
    parser.add_argument('-action','--action',help=' Post, Get or Put', required=True)
    parser.add_argument('-endpoint','--endpoint', help=' Enter endpoint name.', required=True)
    parser.add_argument('-file_path','--file_path', help=' Enter action file path.', required=True)
    return vars(parser.parse_args())

def cli():
    """
    Command Line function.
    """
    import json
    arguments = make_parser()
    with open(arguments.file_path) as action_data:
        arguments.data = json.load(action_data)
    run(arguments)
