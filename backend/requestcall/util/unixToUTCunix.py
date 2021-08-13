import datetime


def timeToUnix(hour,minute):

    now = datetime.datetime.today().strftime('%Y-%m-%d')
    year = int(now[0:4])
    month = int(now[5:7])
    day = int(now[8:10])
    # multiply 1000 for milisecond stuff
    unixLocal = int(datetime.datetime(year,month,day, hour,minute,0).strftime('%s'))*1000
    # UTCtimeUNIX = unixConvertor(month,day,unixLocal)
    return unixLocal


def unixConvertor(month,day,unixTime):

    daylightTime1 = (16200)*1000
    daylightTime2 = (12600)*1000
    if month > 3 and month < 9 :
        unixTime += daylightTime1
    elif month > 9 or month < 3 : 
        unixTime += daylightTime2
    elif month == 3:
        if day >= 22:
            unixTime += daylightTime1
        else:
            unixTime += daylightTime2
    elif month == 9:
        if day >= 22:
            unixTime += daylightTime2
        else:
            unixTime += daylightTime1
    return unixTime

def engDateToUnix(year,month,day,hour,minute):

    unix = int(datetime.datetime(year,month,day, hour,minute,0).strftime('%s'))*1000
    unix = unixConvertor(month,day,unix)
    return unix
