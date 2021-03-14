import json
import csv
from itertools import product
import copy
import datetime
import sys

path = sys.argv[1]

connection = []

with open(path) as f:
    reader = csv.reader(f)

    for row in reader:

        num_synapse_list = [int(str_num) for str_num in row[2][1:-1].replace(" ", '').split(",")]
        
        template_dict = {"comment": "hoge","target": "hoge","sources": [{"source": "hoge","section": {"name": "axon","point": 0.5},"windowsize": -9999,"num_synapse": [-9999]}],"synapse": {"suffix": "gsyn2","section": {"name": "axon","point": 0.5},"value": "vpre"},"synapse_opt": {"vth": -9999,"vre": -9999,"k": -9999,"gsat": -9999,"delay": -9999}}
        sources_template = {"source": "hoge","section": {"name": "axon","point": 0.5},"windowsize": -9999,"num_synapse": [-9999]}

        template_dict["comment"] = str(row[0]) + "To" + str(row[1])
        template_dict["target"] = str(row[1])
        sources_template["source"] = str(row[0])
        sources_template["windowsize"] = int(row[9])
        tmp_list = []
        sources_template["num_synapse"] = num_synapse_list
        tmp_list.append(sources_template)
        template_dict["sources"] = tmp_list
        template_dict["synapse_opt"]["vth"] = int(row[4])
        template_dict["synapse_opt"]["vre"] = int(row[3])
        template_dict["synapse_opt"]["k"] = float(row[5])
        template_dict["synapse_opt"]["gsat"] = row[6]
        template_dict["synapse_opt"]["delay"] = row[8]

        connection.append(template_dict)


neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,-1],[-1,1]]
windowsize0 = [[0,0]]
windowsize1 = [[0,0],[1,0],[1,-1],[0,-1],[-1,0],[-1,1],[0,1]]
windowsize2 = [[0,0],[1,0],[1,-1],[0,-1],[-1,0],[-1,1],[0,1],[1,1],[2,0],[2,-1],[2,-2],[1,-2],[0,-2],[-1,-1],[-2,0],[-2,1],[-2,2],[-1,2],[0,2]]
windows = {}
windows["0"] = windowsize0
windows["1"] = windowsize1
windows["2"] = windowsize2

w = 10
h = 10
cells = []

net = []
for con in connection:
    target = con["target"]
#    print(target)
    for src in con["sources"]:
#        print(src)
        for x,y in product(range(w),range(h)):
            n = {}
            n["target_synapse"] = con["synapse"]
            n["synapse_opt"] = con["synapse_opt"]
#            print(windows[str(src["windowsize"])])
            for i,coord in enumerate(windows[str(src["windowsize"])]):
                if x + coord[0]< 0 or x + coord[0]>= w:
                    continue
                if y + coord[1]< 0 or y + coord[1]>= h:
                    continue
                if con["target"] == "T4a" and src["source"] == "Mi1":
                    if x == 3 and y == 3:
                        print("{},{},{}".format(x,y,coord))
                        print("{},{}".format(x+coord[0], y+coord[1]))
                n["target_cellname"] = con["target"] + "," + str(x) + "," + str(y)
                n["source_cellname"] = src["source"] + "," + str(x+coord[0]) + "," + str(y+coord[1])
                if con["target"] == "T4a" and src["source"] == "Mi1":
                    if x == 3 and y == 3:
                        print(n["source_cellname"])

                n["source_section"] = src["section"]
                synlist = src["num_synapse"]
                n["synapse_opt"]["numsyn"] = synlist[i]
                if synlist[i] == 0:
                    continue
                if "source_opt" in src:
                    n["source_opt"] = src["source_opt"]
                else:
                    n["source_opt"] = {}
                net.append(copy.deepcopy(n))

dt_now = datetime.datetime.now()
name = dt_now.strftime('%Y_%m_%d_%H_%M_%S')

with open(name + "connection.json","w") as f:
    json.dump(net,f, indent=4, sort_keys=True, separators=(',', ': '))