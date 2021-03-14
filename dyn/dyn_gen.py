import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]

layer_name = ["R1-6","L1","L2","L3","L4","L5","Mi1","Tm1","Tm2","Tm4","Tm9", "CT1", "C2","C3","T5a","T5b","T5c","T5d"]
dynamics = ["R","L","L","L","L","L","Mi1","Tm1","Tm2","Tm4","Tm9", "CT1", "C3","C3","T5","T5","T5","T5"]
# layer size
w = 10
h = 10
cells = []
for i,name in enumerate(layer_name):
    for x,y in product(range(w),range(h)):
        cell = {}
        cell["cellname"] = name + "," + str(x) + "," + str(y)
        cell["celltype"] = dynamics[i]
        if dynamics[i] == "C3":
            cell["params"] = {"cm": 800000}
        else:
            cell["params"] = {}
        cells.append(cell)

with open("dyn.json","w") as f:
    json.dump(cells,f)
