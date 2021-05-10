def fixData(input):
    # print((input))
    result = []
    sum = 0
    for d in input:
        sum = 0
        if d["Signal_EMA200"] == "NaN":  
            d["Signal_EMA200"] = 0
        sum+=d["Signal_EMA200"]
        if d["Signal_EMA10"] == "NaN": 
            d["Signal_EMA10"] =0
        sum+=d["Signal_EMA10"]

        if d["Signal_HMA"] == "NaN": 
            d["Signal_HMA"] =0
        sum+=d["Signal_HMA"]

        if d["Signal_ICHI"] == "NaN": 
            d["Signal_ICHI"] =0
        sum+=d["Signal_ICHI"]

        if d["Signal_EMA50"] == "NaN": 
            d["Signal_EMA50"] =0
        sum+=d["Signal_EMA50"]

        if d["Signal_EMA5"] == "NaN": 
            d["Signal_EMA5"] =0
        sum+=d["Signal_EMA5"]

        if d["Signal_EMA20"] == "NaN": 
            d["Signal_EMA20"] =0
        sum+=d["Signal_EMA20"]

        if d["Signal_KETLER"] == "NaN": 
            d["Signal_KETLER"] =0
        sum+=d["Signal_KETLER"]

        if d["Signal_MACD"] == "NaN": 
            d["Signal_MACD"] =0
        sum+=d["Signal_MACD"]

        if d["Signal_EMA100"] == "NaN": 
            d["Signal_EMA100"] =0
        sum+=d["Signal_EMA100"]

        if d["Signal_Awesome"] == "NaN": 
            d["Signal_Awesome"] =0
        sum+=d["Signal_Awesome"]

        if d["Signal_CCI"] == "NaN": 
            d["Signal_CCI"] =0
        sum+=d["Signal_CCI"]

        if d["Signal_MFI"] == "NaN": 
            d["Signal_MFI"] =0
        sum+=d["Signal_MFI"]

        if d["Signal_MOM"] == "NaN": 
            d["Signal_MOM"] =0
        sum+=d["Signal_MOM"]

        if d["Signal_PSAR"] == "NaN": 
            d["Signal_PSAR"] =0
        sum+=d["Signal_PSAR"]

        if d["Signal_RSI"] == "NaN": 
            d["Signal_RSI"] =0
        sum+=d["Signal_RSI"]

        if d["Signal_Stoch"] == "NaN": 
            d["Signal_Stoch"] =0
        sum+=d["Signal_Stoch"]

        if d["Signal_StochRSI"] == "NaN": 
            d["Signal_StochRSI"] =0
        sum+=d["Signal_StochRSI"]

        if d["Signal_Ultimate"] == "NaN": 
            d["Signal_Ultimate"] =0
        sum+=d["Signal_Ultimate"]

        if d["Signal_VAMA"] == "NaN": 
            d["Signal_VAMA"] =0
        sum+=d["Signal_VAMA"]

        if d["Signal_Williams"] == "NaN": 
            d["Signal_Williams"] =0
        sum+=d["Signal_Williams"]

        if d["Signal_SMA50"] == "NaN": 
            d["Signal_SMA50"] =0
        sum+=d["Signal_SMA50"]

        if d["Signal_SMA5"] == "NaN": 
            d["Signal_SMA5"] =0
        sum+=d["Signal_SMA5"]

        if d["Signal_SMA200"] == "NaN": 
            d["Signal_SMA200"] =0
        sum+=d["Signal_SMA200"]

        if d["Signal_SMA20"] == "NaN": 
            d["Signal_SMA20"] =0
        sum+=d["Signal_SMA20"]

        if d["Signal_SMA10"] == "NaN": 
            d["Signal_SMA10"] =0
        sum+=d["Signal_SMA10"]

        if d["Signal_SMA100"] == "NaN": 
            d["Signal_SMA100"] = 0
        sum+=d["Signal_SMA100"]

        d["sum"] = sum
        result.append({"persiandate":d["persiandate"],"firm":d["firm"],"ticker":d["ticker"],"sum":sum })
    
    final = sorted(result, key=lambda x : x['sum'], reverse=True)
    highest = final[0:10]
    final = sorted(result, key=lambda x : x['sum'], reverse=False)
    lowest = final[0:10]
    return [highest,lowest]