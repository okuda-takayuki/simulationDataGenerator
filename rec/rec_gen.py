import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]

# layer_name = ["R1-6","L1","L2","L3","L4","L5","Mi1","Tm1","Tm2","Tm4","Tm9","CT1","C2","C3","T5a","T5b","T5c","T5d"]
# dynamics = ["R","L","L","L","L","L","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","Mi1","C3","T4","T4","T4","T4"]
# layer size
w = 10
h = 10

with open("rec/record_position.json","r") as f:
    recs = json.load(f)

cells = []
for rec in recs:
    for x,y in product(range(w),range(h)):
        conf = {}
        conf["target_cellname"] = rec["target"] + "," + str(x) + "," + str(y)
        conf["section"] = rec["section"]
        cells.append(conf)

with open("2021-02-02-7/rec.json","w") as f:
    json.dump(cells,f, indent=4, sort_keys=True, separators=(',', ': '))
