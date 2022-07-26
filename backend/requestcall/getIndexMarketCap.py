import requests
import json


def IndexMarketCapRequest():
    resp = requests.get('http://185.231.115.223:3000/View_IndexMarketCap')
    if resp.status_code == 200:
        js = json.loads(resp.text)
        result = dataAlter(js)

        return (result)
    else:
        return "noData"


def dataAlter(input):
    PieChartTopIndustries = []
    PieChartOthersIndustries = []
    PiechartTopMarketCaps = []
    PiechartOtherMarketCaps = []
    PieChartTopNames = []
    PieChartOtherNames = []
    PieChartOtherindexID = []
    PieChartTopindexID = []
    marketCapOthersSum = 0
    pieData = sorted(input, key=lambda x: x['marketCap'], reverse=True)
    barData = sorted(input, key=lambda x: x['TradeValue'], reverse=True)
    for i, item in enumerate(pieData):
        if (i < 9):
            # PieChartTopIndustries.append(item)
            PiechartTopMarketCaps.append(item["marketCap"])
            PieChartTopNames.append(item["persianName"])
            PieChartTopindexID.append(item["indexID"])
        else:
            PiechartOtherMarketCaps.append(item["marketCap"])
            marketCapOthersSum += item["marketCap"]
            # PieChartOthersIndustries.append(item)
            PieChartOtherNames.append(item["persianName"])
            PieChartOtherindexID.append(item["indexID"])

    PieChartData = {"TopIndustries": {"indexID": PieChartTopindexID, "persianName": PieChartTopNames, "marketCap": PiechartTopMarketCaps},
                    "OtherIndustries": {"marketCapSum": marketCapOthersSum, "indexID": PieChartOtherindexID, "persianName": PieChartOtherNames, "marketCap": PiechartOtherMarketCaps}}

    barData = barData[0:6]
    # print(barData)
    BarChartTradeValue = []
    BarChartNames = []
    BarChartindexID = []
    check = []
    for item in barData:
        BarChartindexID.append(item["indexID"])
        BarChartNames.append(item["persianName"])
        BarChartTradeValue.append(item["TradeValue"])
    BarChartData = {"indexID": BarChartindexID,
                    "persianName": BarChartNames, "TradeValue": BarChartTradeValue}

    result = {"PieChart": PieChartData,
              "BarChart": BarChartData}

    return result

# IndexMarketCapRequest()
