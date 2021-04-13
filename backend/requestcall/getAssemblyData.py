import requests
import json
# import pandas as pd


def firstStepAssembly(identifier):
    url = ""
    if identifier.get("Type") == "AssemblyGeneral":
        url = "http://130.185.74.40:3000/rpc/assemblygenerallist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    elif identifier.get("Type") == "AssemblyExtra":
        url = "http://130.185.74.40:3000/rpc/assemblyextralist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    elif identifier.get("Type") == "AssemblyGeneralExtra":
        url = "http://130.185.74.40:3000/rpc/assemblygenerallist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    elif identifier.get("Type") == "d":
        url = "http://130.185.74.40:3000/rpc/assemblyinvitationgenerallist?a="+identifier.get("tickerID")+"&b="+identifier.get("endDate")+"&c="+identifier.get("startDate")
    
    # print(identifier.get("Type"))
    # print(identifier.get("tickerID"))
    # print(identifier.get("endDate"))
    # print(identifier.get("startDate"))


    print(url)
    if url:
        resp = requests.get(url)
        if resp.status_code == 200:
            return json.loads(resp.text)
        else:
            return "noData"

def secondStepAssembly(identifier, Type):
    links = {}
    result = []
    head = {'Accept-Profile':'codalreports'} 
    #-----------------------------------------------
    if Type == 'AssemblyGeneral':
        links = {
                "Statement":"http://130.185.74.40:3000/View_AG_Statement?SummaryID=eq." +str(identifier),

                "Cheif":"http://130.185.74.40:3000/View_AG_Chief?SummaryID=eq." +str(identifier),

                "Shareholders":"http://130.185.74.40:3000/View_AG_Shareholders?SummaryID=eq." +str(identifier),

                "CEO":"http://130.185.74.40:3000/View_AG_Ceo?SummaryID=eq." +str(identifier),

                "Board":"http://130.185.74.40:3000/View_AG_Board?SummaryID=eq." +str(identifier),

                "NewBoard":"http://130.185.74.40:3000/View_AG_NewBoard?SummaryID=eq." +str(identifier),

                "Wage":"http://130.185.74.40:3000/View_AG_Wage?SummaryID=eq." +str(identifier),

                "Summary":"http://130.185.74.40:3000/View_AG_?ID=eq." +str(identifier)
        }
        for link in links.values():
            resp = requests.get(link,headers = head)
            if resp.status_code == 200:
                result.append(json.loads(resp.text))
            else: 
                result.append("noData")
        return result
        
    #-----------------------------------------------
    elif Type == 'AssemblyExtra':
        links = {
            "IC" : "http://130.185.74.40:3000/View_AE_IC?SummaryID=eq." + str(identifier),
            "Chief": "http://130.185.74.40:3000/View_AE_Chief?SummaryID=eq."+ str(identifier),
            "Shareholder": "http://130.185.74.40:3000/View_AE_Shareholders?SummaryID=eq." + str(identifier),
            "Summary": "http://130.185.74.40:3000/View_AE_?ID=eq."+ str(identifier)

        }
        for link in links.values():
            resp = requests.get(link,headers = head)
            if resp.status_code == 200:
                result.append(json.loads(resp.text))
            else: 
                result.append("noData")
        return result
    #-----------------------------------------------
    elif Type == 'AssemblyGeneralExtra':
        links = {
                "Statement":"http://130.185.74.40:3000/View_AGE_Statement?SummaryID=eq." +str(identifier),

                "Cheif":"http://130.185.74.40:3000/View_AGE_Chief?SummaryID=eq." +str(identifier),

                "Shareholders":"http://130.185.74.40:3000/View_AGE_Shareholders?SummaryID=eq." +str(identifier),

                "CEO":"http://130.185.74.40:3000/View_AGE_Ceo?SummaryID=eq." +str(identifier),

                "Board":"http://130.185.74.40:3000/View_AGE_Board?SummaryID=eq." +str(identifier),

                "NewBoard":"http://130.185.74.40:3000/View_AGE_NewBoard?SummaryID=eq." +str(identifier),

                "Wage":"http://130.185.74.40:3000/View_AGE_Wage?SummaryID=eq." +str(identifier),

                "Summary":"http://130.185.74.40:3000/View_AGE_?ID=eq." +str(identifier)
        }
        for link in links.values():
            resp = requests.get(link,headers = head)
            if resp.status_code == 200:
                result.append(json.loads(resp.text))
            else: 
                result.append("noData")
        return result
    #-----------------------------------------------
    # elif Type == 'd':
    #     pass
    #-----------------------------------------------
    
    # dict={}
    # final=[]
    # Shareholders=[]
    # Cheif=[]
    # Summary=[]
    # Ic=[]
    # resp=requests.get('http://130.185.74.40:3000/View_AssemblyExtraDetails?ID=eq.' + str(identifier))

    # JS=json.loads(resp.text)
    # for item in JS:
    #     Shareholders.append({"Shareholders":item["Shareholders"],"ShareCount":item["ShareCount"],"OwnerPercentage":item["OwnerPercentage"]})

    #     Cheif.append({"Name":item["Name"],"Position":item["Position"]})

    #     Summary.append({"report_id":item["report_id"],"ToDate":item["ToDate"],"Correction":item["Correction"],
    #     "CorrectionDetails":item["CorrectionDetails"],"OtherDesc":item["OtherDesc"],"OldActivity":item["OldActivity"],
    #     "NewActivity":item["NewActivity"],"AccordWithSEOStatuteApproved":item["AccordWithSEOStatuteApproved"],
    #     "DecidedClause141Des":item["DecidedClause141Des"],"OldFinancialYearEndDate":item["OldFinancialYearEndDate"],
    #     "NewFinancialYearEndDate":item["NewFinancialYearEndDate"],"OldName":item["OldName"],"NewName":item["NewName"],
    #     "OldAddress":item["OldAddress"],"NewAddress":item["NewAddress"]})

    #     Ic.append({"LastShareCount":item["LastShareCount"],"LastShareNominalValue":item["LastShareNominalValue"],"LastCapital":item["LastCapital"],"CashIncoming_Final":item["CashIncoming_Final"],
    #     "CashIncoming_Ceo":item["CashIncoming_Ceo"],"CashIncoming_Total":item["CashIncoming_Total"],"RetainedEarning_Final":item["RetainedEarning_Final"],"RetainedEarning_Ceo":item["RetainedEarning_Ceo"],"RetainedEarning_Sum":item["RetainedEarning_Sum"],
    #     "Reserves_Final":item["Reserves_Final"],"Reserves_Ceo":item["Reserves_Ceo"],"Reserves_Sum":item["Reserves_Sum"],"Reevaluation_Final":item["Reevaluation_Final"],
    #     "Reevaluation_Ceo":item["Reevaluation_Ceo"],"Reevaluation_Sum":item["Reevaluation_Sum"],"SarfSaham_Final":item["SarfSaham_Final"],"SarfSaham_Ceo":item["SarfSaham_Ceo"],"SarfSaham_Sum":item["SarfSaham_Sum"],
    #     "IncreaseValue_Final":item["IncreaseValue_Final"],"IncreaseValue_Ceo":item["IncreaseValue_Ceo"],"IncreaseValue_Sum":item["IncreaseValue_Sum"],"IncreasePercent_Final":item["IncreasePercent_Final"],"IncreasePercent_Ceo":item["IncreasePercent_Ceo"]})
    # final.append({"Shareholders" : Shareholders,"Cheif": Cheif,"Summary":Summary,"Ic":Ic})
    # ----------------------------------------------------------
    # DF=pd.DataFrame(JS)
    # ShareHolders=DF[['Shareholders','ShareCount','OwnerPercentage']].drop_duplicates().to_json(orient="records")
    # Chief=DF[['Name', 'Position']].drop_duplicates().to_json(orient="records")
    # Summary=DF[['report_id', 'ToDate', 'Correction', 'CorrectionDetails', 'OtherDesc',
    #     'OldActivity', 'NewActivity', 'AccordWithSEOStatuteApproved',
    #     'DecidedClause141Des', 'OldFinancialYearEndDate',
    #     'NewFinancialYearEndDate', 'OldName', 'NewName', 'OldAddress',
    #     'NewAddress']].drop_duplicates().to_json(orient="records")
    # IC=DF[['LastShareCount',
    #     'LastShareNominalValue', 'LastCapital', 'CashIncoming_Final',
    #     'CashIncoming_Ceo', 'CashIncoming_Total', 'RetainedEarning_Final',
    #     'RetainedEarning_Ceo', 'RetainedEarning_Sum', 'Reserves_Final',
    #     'Reserves_Ceo', 'Reserves_Sum', 'Reevaluation_Final',
    #     'Reevaluation_Ceo', 'Reevaluation_Sum', 'SarfSaham_Final',
    #     'SarfSaham_Ceo', 'SarfSaham_Sum', 'IncreaseValue_Final',
    #     'IncreaseValue_Ceo', 'IncreaseValue_Sum', 'IncreasePercent_Final',
    #     'IncreasePercent_Ceo']].drop_duplicates().to_json(orient="records")
    # dict['ShareHolders']=ShareHolders
    # dict['Chief']=Chief
    # dict['Summary']=Summary
    # dict['IC']=IC
    # return json.loads(json.dumps(dict))

