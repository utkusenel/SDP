import pandas as pd
from gurobipy import *

data = pd.read_csv("/Users/utkusenel/Documents/SDP/Parameters.csv", delimiter = ";")
print(data.columns)


sdp_model = Model("sdp_model")
 
for j in range(0,10):
    for t in range(0,12):
      I[j,t]= sdp_model.addVars(vtype=GRB.INTEGER,name="I".format(j,t))   ## Decision variables defined.
      O[j,t] = sdp_model.addVars(vtype=GRB.BINARY,name="O".format(j,t))    ## j is the number of items and t is the number of periods that are forecasted
      OS[j,t] = sdp_model.addVars(vtype=GRB.INTEGER,name="OS".format(j,t))
      ### PARAMETERS
      SS = data.iloc[j,23] ## safety stock parameter
      ROP = data.iloc[j,22]
      ##DDL = data.


