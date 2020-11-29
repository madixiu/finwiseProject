
import requests
import json
# from .util.Convereter_trunc import truncater, converter
import time
def Top5MostViewed():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewTop5MostViewed',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")
def ImpactOnIndex():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewImpactOnIndex',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data") 
def getStatisticsTicker(identifier):
    head = {'Accept-Profile':'public'}
    resp = requests.get('http://37.152.180.99:3000/rpc/statisticsticker?a='+str(identifier),headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")               
def highestTvolumes():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewHighestTradeVolumes',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestTvalues():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/ViewHighestTradeValues',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestDemands():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_HighestDemands',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")        
def highestSupplies():
    head = {'Accept-Profile':'marketwatch'}
    resp = requests.get('http://37.152.180.99:3000/View_HighestSupplies',headers=head)
    if resp.status_code == 200:

        # return(resp.text)
        return (json.loads(resp.text))
        # return(json.loads(resp.text))
    else:
        return("No Data")                                        