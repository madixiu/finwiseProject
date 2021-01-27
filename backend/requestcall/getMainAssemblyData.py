import requests
import json

def AssemblyListData():
    head = {'Accept-Profile':'codalreports'} 
    resp = requests.get("http://185.97.117.60:3000/View_AllAssembly_List",headers = head)
    js = json.loads(resp.text)
    return js


def AssemblyTableData():
    pass