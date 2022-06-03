from datetime import datetime
from datetime import date
import ast
f = open("latest-output.txt", "r")
lines=f.readlines()
for line in lines :
#split the each index with the ";"##
    linesplit=line.split(";")
# print(linesplit)
    pod=linesplit[0]
    teamfull=linesplit[1]
    res = ast.literal_eval(teamfull)
#print(type(res))
    team=res["app"]
#print(team)
    DateTime=linesplit[2]
    DateTimeSplit=DateTime.split("T")
    Date=DateTimeSplit[0]
    Status=linesplit[3]
    if(team =="team_system"):
       LabelValueCheck=True
    else:
       LabelValueCheck=False
#print(pod)
#print(team)
#print(Date)
#print(Status)
    if(Status == "Running"  ) :
        StatusCheck=True
    else:
        StatusCheck=False
    if("bitnami" in linesplit[4]):
        ImageCheck=True
    else:
        ImageCheck=False
    if(StatusCheck == False):
        DateFormat=datetime.fromisoformat(Date)
        today = datetime.now()
        result=(today-DateFormat)
        DaysCount=(result.days)
        if(DaysCount>=7):
#print("System is down for more than 7 days")
            StatusCheck=False
            
        else:
#print("System is down for less than 7 days")
            StatusCheck=True
    ImageName=linesplit[4].replace("\n","")
    LabelValueCheck_Dict={"name": team,"valid":LabelValueCheck}
    ImageCheck_Dict={"name": ImageName,"valid":ImageCheck}
    StatusCheck_Dict={"name": "recent_start_time", "valid":StatusCheck}
    rule_evaluation_list=[ImageCheck_Dict,LabelValueCheck_Dict,StatusCheck_Dict]
    Dict={"pod": pod, "rule_evaluation":rule_evaluation_list}
    print(Dict)
    
