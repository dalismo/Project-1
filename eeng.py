# Import modules
import numpy as np
import pandas as pd

# Set path for file and open CSV 
filepath = "../Project-1/Resources/California Mortality1.txt"
file = pd.read_csv(filepath, delimiter="\t")
file.to_csv("California_Mortality_1.csv")
cali_mortality_df = pd.read_csv("../Resources/California Mortality1.csv")


cali_mortality_df