# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 04:20:51 2020

@author: user
"""


"""

@author: Justin

Aim : To determine the most popular transportation option in Singapore
        1. Over the years
        2. in 2016

Ridership data:
https://data.gov.sg/dataset/public-transport-utilisation-average-public-transport-ridership

"""

import requests
import matplotlib.pyplot as plt

plt.style.use("seaborn")


#--- getting data from the internet ---#
transport_data = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=552b8662-3cbc-48c0-9fbb-abdc07fb377a&limit=88")

#--- to check data text ---#
#print(transport_data)
#print(transport_data.text)

#--- to convert to json dictionary. To organise & view text information & get dictionary keys ---#
transport_json = transport_data.json()
#print(transport_json)
#transport_json.keys()
#transport_json["result"].keys()

#--- Stratify ridership by year ---#
years = {}

for record in transport_json["result"]["records"]:
    if record["year"] not in years:
        years[record["year"]] = {}
    if record["type_of_public_transport"] not in years[record["year"]]:
        years[record["year"]][record["type_of_public_transport"]] = {}
    try:
        years[record["year"]][record["type_of_public_transport"]] = int(record["average_ridership"])
    except:
        years[record["year"]][record["type_of_public_transport"]] = 0

#--- Assign ridership to individual transportation ---#
yearlist = list(years.keys())
year=[]
MRT=[]
LRT=[]
Bus=[]
Taxi=[]

for i in yearlist:
    year.append(i)
    for type_of_public_transport in years[i]:
        if type_of_public_transport=="MRT":
            MRT.append(years[i][type_of_public_transport])
        if type_of_public_transport=="LRT":
            LRT.append(years[i][type_of_public_transport])
        if type_of_public_transport=="Bus":
            Bus.append(years[i][type_of_public_transport])
        if type_of_public_transport=="Taxi":
            Taxi.append(years[i][type_of_public_transport])
#can use elif instead of if
         
#--- plot ridership for all years ---#
plt.figure(figsize=(10,5)) 
plt.title("Average Daily Public Transport Ridership over the years") 
plt.xlabel("Year") 
plt.ylabel("Average Ridership ('000 passanger trips per day)")
plt.plot(year, MRT, ".-", label="MRT")
plt.plot(year, LRT, ".-", label="LRT")
plt.plot(year, Bus, ".-", label="Bus")
plt.plot(year, Taxi, ".-", label="Taxi")
plt.tight_layout() 
plt.legend(loc='best')
plt.show()
#plt.savefig("%s_Average_Daily_Public_Transport_Ridership_over_years.png" % type_of_public_transport.lower(), dpi=300) # save the scatter plot

#---plot ridership for year 2016---#
data=years["2016"]
plt.figure(figsize=(10,5))
plt.bar(range(len(data)),data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.title("Average Daily Public Transport Ridership for Year 2016") 
plt.xlabel("Type of Public Transport") 
plt.ylabel("Average Ridership ('000 passanger trips per day)")
plt.show()
#plt.savefig("Average Daily Public Transport Ridership for Year 2016.png", dpi=300) # save the bar plot

