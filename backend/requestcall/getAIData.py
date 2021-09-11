import requests
import json
import time
def getOneWeekLSTM(identifier):
    ct=0
    while ct<3:
        head = {'Accept-Profile':'ai'}
        resp = requests.get('http://5.253.27.108:3000/LSTM_OneStock?firm=eq.'+str(identifier)+'&limit=25&'+'&order=date.desc',headers=head)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
        else:
            time.sleep(2)
            ct=ct+1
        
    return []    