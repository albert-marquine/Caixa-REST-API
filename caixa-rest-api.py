#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Caixa transactions REST API testing script.

import subprocess,argparse,json

class api_action:
    def post(endpoint,data):
        if data['endpoint'] != '':
            query = subprocess.run(['curl','-X POST', '-H "Accept: application/json"', 'https://16.170.244.46/api/'+endpoint+'/'+data['endpoint'], '-d'+data], shell=True, check=True)
        else:
            query = subprocess.run(['curl','-X POST', '-H "Accept: application/json"', 'https://16.170.244.46/api/'+endpoint, '-d'+data], shell=True, check=True)
        return(query)

    def get(endpoint,data):
        query = subprocess.run(['curl','-X GET', '-H "Accept: application/json"', 'https://16.170.244.46/api/'+endpoint+'/'+data], shell=True, check=True)
        return(query)

    def put(endpoint,data):
        query = subprocess.run(['curl','-X PUT', '-H "Accept: application/json"', 'https://16.170.244.46/api/'+endpoint, '-d'+data], shell=True, check=True)
        return(query) 

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Caixa's transactions API testing script.")
    parser.add_argument('-a','--action',help=' Post, Get or Put', required=True)
    parser.add_argument('-endpoint','--endpoint', help=' Enter endpoint name', required=True)
    parser.add_argument('-file_path','--file_path', help=' Enter action file path.', required=True)

    args = vars(parser.parse_args())

    action = args['action']
    endpoint = args['endpoint']
    file_path = args['file_path']
 
    with open(file_path) as action_data:
        data = json.load(action_data)
   
    try:
        if action.upper() == 'POST':
            result = api_action.post(endpoint,data)
            print(result)
        elif action.upper() == 'GET':
            result = api_action.post(endpoint,data)
            print(result)
        elif action.upper() == 'PUT':
            result = api_action.post(endpoint,data)
            print(result)
        else:
            raise  Exception("Uknown parameter: "+action+".\nExpecting parameters: POST, GET, PUT.")
    
    except Exception as error:
        print(error)
