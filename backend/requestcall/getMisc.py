import requests
import json
import datetime
import pandas as pd
import trendln


def TrendSuppData(identifier):
    ct = 0
    while ct < 3:
        head = {'Accept-Profile': 'public'}
        resp = requests.get(
            'http://185.231.115.223:3000/rpc/adjustedpricestyp3?a='+str(identifier), headers=head)
        if resp.status_code == 200:
            DF = pd.DataFrame(json.loads(resp.text))
            DF.sort_values(by='engdate', inplace=True)
            DF = DF.tail(100)
            DF.reset_index(inplace=True, drop=True)
            for i in DF.columns:
                if i in ['adjustedhigh', 'adjustedlow', 'adjustedfirst', 'adjustedclosing']:
                    DF[i] = DF[i].apply(lambda x: round(x, 0))
            # C=pd.Series(data=DF['adjustedclosing'].tolist(),index=DF.engdate)
            H = pd.Series(data=DF['adjustedhigh'].tolist(), index=DF.engdate)
            L = pd.Series(data=DF['adjustedlow'].tolist(), index=DF.engdate)
            # mins, maxs = trendln.calc_support_resistance(N,accuracy=8)
            # minimaIdxs, pmin, mintrend, minwindows = trendln.calc_support_resistance((L, None),accuracy=8) #support only
            mins, maxs = trendln.calc_support_resistance((L, H), accuracy=8)
            (minimaIdxs, pmin, mintrend, minwindows), (maximaIdxs,
                                                       pmax, maxtrend, maxwindows) = mins, maxs
            Identicals = []
            Minlines = []
            for i in mintrend:
                linetemp = []
                # cont=True
                # for j in i[0]:
                #     if j in Identicals:
                #         cont=False
                #     else:
                #         Identicals.append(j)
                # if cont:
                for k in i[0]:
                    linetemp.append(
                        {'x': DF.iloc[k].engdate, 'y': DF.iloc[k].adjustedlow})
                Minlines.append(linetemp)
            Maxlines = []
            for i in maxtrend:
                linetemp = []
                for k in i[0]:
                    linetemp.append(
                        {'x': DF.iloc[k].engdate, 'y': DF.iloc[k].adjustedhigh})
                Maxlines.append(linetemp)
            return {'candles': json.loads(DF.to_json(orient='records')), 'supppoints': Minlines, 'resistancepoints': Maxlines}
        else:
            ct = ct+1
    return "noData"
