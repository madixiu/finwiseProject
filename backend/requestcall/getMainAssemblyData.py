import requests
import json
from .util.Convereter_trunc import converterFAtoEN
def AssemblyListData():
    head = {'Accept-Profile':'codalreports'} 
    resp = requests.get("http://185.97.117.60:3000/View_AllAssembly_List",headers = head)
    js = json.loads(resp.text)
    return js


def AssemblyTableData():
    pass

def getCalendarData():
    head = {'Accept-Profile':'codalreports'} 
    resp = requests.get("http://185.97.117.60:3000/View_AllAssembly_Calendar",headers = head)
    js = json.loads(resp.text)
    for item in js:
        item["PublishTime"] = (converterFAtoEN(item["PublishTime"])).strip()
    return js


# print(getCalendarData())