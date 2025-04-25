import json


"""
[
  {
    "id": 1,
    "city": "Port Blair",
    "district": "South Andaman",
    "std-code": 3192,
    "state": "Andaman and Nicobar Islands",
    "gst-state-code": "AN",
    "iso_3166-2": "IN-AN",
    "population": 108058,
    "rank": 423,
    "latitude": 11.6233774,
    "longitude": 92.7264828,
    "altitude": 16.12903976
  },
  {
"""

with open ("/home/neom/B.Tech/8th-Semester/Project/Datasets_Cleaning/cities.json","r") as f :
    data = json.load(f)
    unique_states = list(set(item["state"] for item in data))
    print(unique_states,len(unique_states))
