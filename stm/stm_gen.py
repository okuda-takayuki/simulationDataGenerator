import json
import numpy as np
from itertools import product
neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]

layer_name = ["R1-6","L1","L2","L3","L4","L5","Mi1","Tm1","Tm2","Tm4","Tm9","CT1","C2","C3","T5a","T5b","T5c","T5d"]
dynamics = ["R","L","L","L","L","L","Mi1","Mi1","Mi1","Mi1","Mi1","C3","Mi1","C3","T4","T4","T4","T4"]
# layer size
w = 4
h = 4
stims = []
stim_timing = [[300,1100,1]]
for st in stim_timing:
    for x,y in product(range(w),range(h)):
        stim = {}
        stim["stimulator"] = "BellCurrent"
        stim["target_cellname"] = "R1-6" + "," + str(x) + "," + str(y)
        stim["section"] = {"name":"axon","point":0.5}
        stim["opt"] = {}
        stim["opt"]["st"] = st[0]
        stim["opt"]["en"] = st[1]
        stim["opt"]["amp"] = st[2]
        stim["opt"]["slope"] = 0.03
        stims.append(stim)

with open("2020-12-31/wholestm.json","w") as f:
    json.dump(stims,f)
