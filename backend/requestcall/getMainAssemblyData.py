import requests
import json
from .util.Convereter_trunc import converterFAtoEN
def AssemblyListData():
    head = {'Accept-Profile':'codalreports'} 
    resp = requests.get("http://185.8.172.68:3000/View_AllAssembly_List",headers = head)
    if resp.status_code == 200:
        js = json.loads(resp.text)
        return js
    else:
        return "noData"


def AssemblyTableData():
    pass

def getCalendarData():
    head = {'Accept-Profile':'codalreports'} 
    resp = requests.get("http://185.8.172.68:3000/View_AllAssembly_Calendar",headers = head)
    if resp.status_code == 200:
        js = json.loads(resp.text)
        for item in js:
            item["PublishTime"] = (converterFAtoEN(item["PublishTime"])).strip()
        return js
    else:
        return "noData"


# print(getCalendarData())