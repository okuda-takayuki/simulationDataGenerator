import json
import datetime
import os

dt_now = datetime.datetime.now()
name = dt_now.strftime('%Y_%m_%d_%H_%M_%S')

run = {
  "description" : "Hodgkin-Huxlay model Neuron spike and voltage recording simulation sample",
  "dynamics_def_path": "testdata/" + name + "/dyn.json",
  "stim_setting_path": "testdata/" + name + "/delay1direct0_stm.json",
  "connection_def_path": "testdata/" + name + "/" + "-nwk10by10.json",
  "record_setting_path": "testdata/" + name + "/rec.json",
  "v_init": -60,
  "tstop": 3500,
  "downsample": 10
}

os.mkdir("../"+name)
with open("../"+ name + "/run.json","w") as f:
    json.dump(run,f)