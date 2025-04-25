import json 

k = []
with open("Datasets_Cleaning/state.json","r") as f:
    k = json.load(f)
    print(k)


