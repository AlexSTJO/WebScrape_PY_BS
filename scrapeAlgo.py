import json
import ast

def storeData():
    f = open("productinfo.txt", "r+")
    data = {}
    count = 1

    while True:
        item = f.readline()
        if item == "":
            break
        data["item"+ str(count)] = ast.literal_eval(item)
        count += 1
    f.truncate(0)
    return data

def recAlgo(tags):
    data = storeData()
    recItems = dict(data)
    if tags['rating'] != "":
        for key in data:
            if float(tags['rating']) > float(data[key]["rating"][0:3]):
                recItems.pop(key)
                
            else:
                recItems[key]['points'] = float(recItems[key]['rating'][0:3]) * 20
    
    data = dict(recItems)
    pList = []
    if tags['pricing'] != "":

        for key in data:
            if float(tags['pricing']) != "" and float(tags['pricing']) < float(data[key]["pricing"]):
                recItems.pop(key)
            else:   
                pList.append(float(recItems[key]['pricing']))
    pList.sort(reverse = True)
    if tags['pricing'] != "" or tags['rating'] != "":
        for key in recItems:
            recItems[key]['points'] += pList.index(float(recItems[key]['pricing']))
            print(recItems[key])

    print(recItems)
            
    
    
                

