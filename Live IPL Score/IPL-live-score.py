import urllib.request
import json

data=urllib.request.urlopen("https://www.cricbuzz.com/match-api/livematches.json").read()
teams1=""
teams2=""
score=""
status=""
for i in json.loads(data)["matches"]:
    match_type=json.loads(data)["matches"][i]["series"]["type"]
    state = json.loads(data)["matches"][i]["state"]
    if match_type == "IPL" and state != "mom" and state != "preview" :
        print("Live Match: \n")
        teams1 = json.loads(data)["matches"][i]["team1"]["name"]
        teams2 = json.loads(data)["matches"][i]["team2"]["name"]
        score = json.loads(data)["matches"][i]["score"]["batting"]["score"]
        status = json.loads(data)["matches"][i]["status"]
        print(teams1 +" vs "+ teams2)
        print(score)
        print(status + "\n")
    if match_type == "IPL" and state == "mom" :
        print("\n Recent Matches : \n")
        teams1 = json.loads(data)["matches"][i]["team1"]["name"]
        teams2 = json.loads(data)["matches"][i]["team2"]["name"]
        status = json.loads(data)["matches"][i]["status"]
        print(teams1 +" vs "+ teams2)
        print(status)
        print("\n")
    if match_type == "IPL" and state == "preview" :
        print("\n To be started soon : \n")
        teams1 = json.loads(data)["matches"][i]["team1"]["name"]
        teams2 = json.loads(data)["matches"][i]["team2"]["name"]        
        print(teams1 +" vs "+ teams2)
        print("\n")
