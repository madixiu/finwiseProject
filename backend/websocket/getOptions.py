import requests
import json
# import pandas as pd
# import ast

def optionRequest():
    resp = requests.get('http://37.152.180.99:3000/callOptionsView')
    if resp.status_code == 200:
        # d=eval(resp.text)
        # p=pd.DataFrame(d)
        # # return (p.to_dict(orient='records'))
        # return json.loads(p.to_dict()).encode('utf-8').decode()
        #return(resp.text)
        print("GETTING CALL OPTION")
        return (resp.text)


def optionFlag():
    resp = requests.get('http://37.152.180.99:3000/Freeze')
    flag = False
    if resp.status_code == 200:
        jsonDATA = json.loads(resp.text)
        flag = jsonDATA[0]['Flag']
        print("FLAG OPTION")

    return flag
    
    