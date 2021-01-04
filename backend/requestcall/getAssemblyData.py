import requests
import json

def firstStepAssembly(identifier):
    url = ""
    if identifier.get("Type") == "a":
        url = "http://185.97.117.60:3000/rpc/assemblygenerallist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    elif identifier.get("Type") == "b":
        url = "http://185.97.117.60:3000/rpc/assemblyextralist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    elif identifier.get("Type") == "c":
        url = "http://185.97.117.60:3000/rpc/assemblygenerallist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    elif identifier.get("Type") == "d":
        url = "http://185.97.117.60:3000/rpc/assemblyinvitationgenerallist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    
    print(identifier.get("Type"))
    print(identifier.get("tickerID"))
    print(identifier.get("endDate"))
    print(identifier.get("startDate"))


    print(url)
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            return json.loads(resp.text)
        else:
            return "noData"
