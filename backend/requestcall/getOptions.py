import pandas as pd
import requests
import json
import pandas as pd
from .util.Convereter_trunc import truncater, converter


def optionRequest():
    try:
        head = {'Accept-Profile': 'options'}
        resp = requests.get(
            'http://185.231.115.223:3000/callOptionsView', headers=head)
        if resp.status_code == 200 and not resp.text == []:
            DF = pd.read_json(resp.text)
            DF.loc[DF['DifferenceToLast'] == -1001, 'ArzandegiLast'] = -1001
            DF.loc[DF['DifferenceToLast'] == -1000, 'ArzandegiLast'] = -1000
            DF.loc[DF['DifferenceToAverage'] == -100001, 'PPP'] = -1001
            DF.loc[DF['DifferenceToAverage'] == -100000, 'PPP'] = -1000
            return cleanOutput(json.loads(DF.to_json(orient="records")))
        else:
            return "noData"
    except:
        return "noData"


# def optionFlag():
#     head = {'Accept-Profile':'options'}
#     resp = requests.get('http://185.231.115.223:3000/Freeze',headers = head)
#     flag = False
#     if resp.status_code == 200:
#         jsonDATA = json.loads(resp.text)
#         flag = jsonDATA[0]['Flag']


#     return flag

def cleanOutput(option):
    # keys = option[0].keys()
    id = 1
    for item in option:
        item["id"] = id
        id += 1
        if isinstance(item['FinalPayment'], float):
            item['FinalPayment'] = truncater(item['FinalPayment'])

        if isinstance(item['TotalValue'], float):
            item['TotalValue'] = truncater(item['TotalValue'])

        if isinstance(item['DifferenceToAverage'], float):
            item['DifferenceToAverage'] = truncater(
                item['DifferenceToAverage'])

        if isinstance(item['averageFairprice'], float):
            item['averageFairprice'] = truncater(item['averageFairprice'])

        if isinstance(item['PPP'], float):
            item['PPP'] = truncater(item['PPP'])

        if isinstance(item['ArzandegiLast'], float):
            item['ArzandegiLast'] = truncater(item['ArzandegiLast'])

        if isinstance(item['DifferenceToLast'], float):
            item['DifferenceToLast'] = truncater(item['DifferenceToLast'])

    option = sorted(
        option, key=lambda x: x['DifferenceToAverage'], reverse=True)

    # converting English numbers to Persian Numbers // disable for now
    # for i in keys:
    #     item[i] = converter(item[i])

    return option


# print(optionRequest())
