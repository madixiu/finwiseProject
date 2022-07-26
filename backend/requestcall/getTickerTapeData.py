import requests
import collections
from datetime import datetime
from time import mktime
from .util.Convereter_trunc import truncater
import json


def TickerTapeData():
    resp = requests.get('http://185.231.115.223:3000/View_Marquee')
    if resp.status_code == 200:
        return (json.loads(resp.text))
    else:
        return "noData"


def IndustryTapeData():
    head = {"Accept-Profile": "indices"}
    resp = requests.get(
        'http://185.231.115.223:3000/View_TapeTicker_Indices', headers=head)
    if resp.status_code == 200:
        js = json.loads(resp.text)
        result = IndustryDataFix(js)
        return (result)
    else:
        return "noData"


def AddUnix(item):
    time = item["HourMinute"].split(":")
    date = item["englishDate"].split("-")
    dt = datetime(int(date[0]), int(date[1]), int(
        date[2]), int(time[0]), int(time[1]), 0, 0)
    unixTime = int(mktime(dt.timetuple()))
    return unixTime


def IndustryDataFix(input):
    temp = []
    nameList = []
    Sorted = []
    result = []
    for item in input:
        nameList.append(item["CorrectName"])

    dups = [item for item, count in collections.Counter(
        nameList).items() if count == 2]
    for item in input:
        if item["CorrectName"] in dups:
            item["unix"] = AddUnix(item)
            temp.append(item)
    temp = sorted(temp, key=lambda x: x["CorrectName"], reverse=False)

    for i in range(0, len(temp), 2):
        if temp[i]["unix"] < temp[i+1]["unix"]:
            Sorted.append(temp[i])
            Sorted.append(temp[i+1])
        else:
            Sorted.append(temp[i+1])
            Sorted.append(temp[i])
    for i in range(0, len(Sorted), 2):
        result.append({"ID": Sorted[i]["indexID"], "ticker": Sorted[i]["CorrectName"], "unix": Sorted[i+1]["unix"],
                      "close": Sorted[i+1]["Value"], "Change": perCentCalc(Sorted[i+1]["Value"], Sorted[i]["Value"])})

    return result


def perCentCalc(x2, x1):
    return truncater(((x2/x1)-1)*100)

# IndustryTapeData()
