'''
This example shows the use of a time dependent decision variable .
In this example the variable is beeing used for choosing between options in the grid connection. The available maximum power for power consumption can be choosen from a list.
The different options come at different prices.
This is beeing done by a decision variable 'connection_choice' in the gridConnection class.
The different options and properties associated with the choice get passed by a dictionary in the following form:
{'opt1':{'price':100,'p_max':500},
 'opt2':{'price':200,'p_max':1000}}
The package automatically generates binary state variables for choosing between the options and continuous state variable for the different properties.
decisionVar.get_result() shwows the chosen option after the optimization as shown below.
'''
# %%
# Imports

import pandas as pd
import numpy as np
from MilPython import *
from LPObjects import *
# %%
# instanciating objects
steps=5
inputdata_dict = {'electricity_price':-np.sin(np.linspace(0, 10*np.pi, steps)) + 2,  # electricity price oscillates around 1
                  'electricity_demand':np.full(steps,500)}                           # constant electricity demand
inputdata = LPInputdata(data=inputdata_dict,dt_h=10/60)
buil = Building(inputdata,bat_price=10)

# %%
# Display the LP-system
buil.show_lp_system()

# %%
# Solve
buil.optimize()
buil.grid.connection_choice.get_result()


#%%
buil2 = Building(inputdata,bat_price=1)
buil2.optimize()
print(f'Lowest total cost with {buil2.bat.E_max.result} Wh battery storage for 1 € / Wh')
buil2.bat.E.plot_result()
# %%
# %%
# Save results to Excel
buil.results_to_excel('results.xlsx')
# %%