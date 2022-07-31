import requests
import json

def getOneWeekLSTM(identifier):
    try:
        head = {'Accept-Profile':'ai'}
        resp = requests.get('http://5.253.27.108:3000/LSTM_OneStock?firm=eq.'+str(identifier)+'&limit=25&'+'&order=date.desc',headers=head,timeout=3.05)
        if resp.status_code == 200 and resp.text!='[]' :
            return (json.loads(resp.text))
    except:
        return []
        
    return []    