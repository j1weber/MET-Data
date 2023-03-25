#Author Info
#Jake Weber, PhD Student
#UCSD -- SIO 
#Mar 23, 2023 

#Script Read data from NOAA NERRS Centralized Data Management Office website:
    #Station Code - TJRTLMET
    #Dates: 12/01/2022 - 03/23/2023
    #Data Type: meteorological
    #Type: Best available dataset



#Importing Required Packages
import pandas as pd

#Path to where the data for #Dates: 12/01/2022 - 03/23/2023 is stored | If you are using this you will have to change the path to contain your credentials. PS: I hope drive keeps its syntax the same so that this is future proofed. 
path = '/Users/jakeweber/Library/CloudStorage/GoogleDrive-j1weber@ucsd.edu/Shared drives/Prather Lab Shared Drive/2. Current Projects/Imperial Beach: Winter 2023 Campaign/MET Data/800513/TJRTLMET.csv'
TJRTLMET_dec22_mar23 = pd.read_csv(path, skiprows=[0, 1])