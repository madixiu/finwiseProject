
import requests
import json
from .util.Convereter_trunc import truncater, converter







def optionRequest():
    head = {'Accept-Profile':'options'}
    resp = requests.get('http://37.152.180.99:3000/callOptionsView',headers = head)
    if resp.status_code == 200:
 
        # return(resp.text)
        return (json.dumps(cleanOutput(json.loads(resp.text))))
        # return(json.loads(resp.text))
    else:
        
        return ("noData")


def optionFlag():
    head = {'Accept-Profile':'options'}
    resp = requests.get('http://37.152.180.99:3000/Freeze',headers = head)
    flag = False
    if resp.status_code == 200:
        jsonDATA = json.loads(resp.text)
        flag = jsonDATA[0]['Flag']
        

    return flag

def cleanOutput(option):
    keys = option[0].keys()
    for item in option:
  
        if isinstance(item['FinalPayment'], float):
            item['FinalPayment'] = truncater(item['FinalPayment'])

        if isinstance(item['TotalValue'], float):
            item['TotalValue'] = truncater(item['TotalValue'])

        if isinstance(item['DifferenceToAverage'], float):
            item['DifferenceToAverage'] = truncater(item['DifferenceToAverage'])

        if isinstance(item['averageFairprice'], float):
            item['averageFairprice'] = truncater(item['averageFairprice'])

        if isinstance(item['PPP'], float):
            item['PPP'] = truncater(item['PPP'])

        if isinstance(item['ArzandegiLast'], float):
            item['ArzandegiLast'] = truncater(item['ArzandegiLast'])

        if isinstance(item['DifferenceToLast'], float):
            item['DifferenceToLast'] = truncater(item['DifferenceToLast'])

        # converting English numbers to Persian Numbers // disable for now
        # for i in keys:
        #     item[i] = converter(item[i])

    
    return option


# print(optionRequest())