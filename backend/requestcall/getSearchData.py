import requests
import json

def SearchData():
    result=''
    try:
        r = requests.get('http://185.231.115.223:3000/View_SearchBar',timeout=5)
        result=json.loads(r.text)
    except Exception as err:
        return ("noData")
    try:
        r2 = requests.get('http://162.55.15.105:3000/View_Search',timeout=5)
        result=result+json.loads(r2.text)
    except Exception as err:
        pass
    return result

    # resp = requests.get('http://185.231.115.223:3000/View_SearchBar',timeout=10)
    # resp2 = requests.get('http://162.55.15.105:3000/View_Search',timeout=10)
    # if resp.status_code == 200 and resp2.status_code==200:
    #     # return (json.loads('['+resp.text[1:-1]+', \n '+resp2.text[1:-1]+']'))
    #     return (json.loads(resp.text)+json.loads(resp2.text))
    # if resp.status_code == 200:
    #     return (json.loads(resp.text))
    # else:
    #     return ("noData")
