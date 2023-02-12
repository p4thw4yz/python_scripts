# Python script
# author - p4thw4yz
# This is a simple python script to intergrate data from your solax solar inverter into
# any program of home automation software you are using or programming

import requests

# These 2 variables can be found after logging into your online solax account
INVERTER = "INVERTERMODELINFORMATION"
TOKENID = "TOKENID"

def getSolar():
    inverter = requests.get("https://www.eu.solaxcloud.com:9443/proxy/api/getRealtimeInfo.do?tokenId="+TOKENID+"&sn="+INVERTER)
    json_data = inverter.json() # convert get request to json
    data = json_data['result'] # Extract results json from get data that was pulled
    return str(data['acpower']) # return given data, this can be modified to anything from the json_data

print(getSolar())