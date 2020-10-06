#!/usr/bin/python3

import requests
#hacky fix for ssl dumbassery
from urllib3.exceptions import InsecureRequestWarning
import json

#hacky fix for ssl dumbassery
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

apikey = 'hahayeahright'
gophishserv = "https://sandbox.choopie:3333"

def getusers(uri,key):
        suffix = '/api/users/'
        heady = {'Authorization': apikey}
        req = requests.get(gophishserv + suffix,headers=heady, verify=False)
        #print(req.text) #debug
        thisjson = json.loads(req.text)
        return thisjson

def getsendprofiles(uri,key):
        suffix = '/api/smtp/'
        heady = {'Authorization': apikey}
        req = requests.get(gophishserv + suffix,headers=heady, verify=False)
        #print(req.text) #debug
        thisjson = json.loads(req.text)
        return thisjson

def gettemplates(uri,key):
        suffix = '/api/templates/'
        heady = {'Authorization': apikey}
        req = requests.get(gophishserv + suffix,headers=heady, verify=False)
        #print(req.text) #debug
        thisjson = json.loads(req.text)
        return thisjson

def getcampaigns(uri,key):
        suffix = '/api/campaigns/'
        heady = {'Authorization': apikey}
        req = requests.get(gophishserv + suffix,headers=heady, verify=False)
        #print(req.text) #debug
        thisjson = json.loads(req.text)
        return thisjson

def getcampaignresults(uri,key):
        thesecamps = []
        campids = []
        getcamps = getcampaigns(uri, key)
        #print(getcamps)
        for ids in getcampaigns(uri, key):
                if ids is not None:
                        campids.append(ids['id'])
        for id in campids:
                suffix = '/api/campaigns/' + str(id) + '/results/'
                heady = {'Authorization': apikey}
                req = requests.get(gophishserv + suffix,headers=heady, verify=False)
                #print(req.text) #debug
                thesecamps.append(json.loads(req.text))
        return thesecamps

def testauth():
        heady = {'Authorization': apikey}
        req = requests.get(gophishserv,headers=heady, verify=False)
        print(req.text)

#print(getusers(gophishserv, apikey))
#print(getsendprofiles(gophishserv, apikey))
#print(gettemplates(gophishserv, apikey))
#print(getcampaigns(gophishserv, apikey))
#print(getcampaignresults(gophishserv, apikey)[0])
