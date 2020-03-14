import numpy as np
import pandas as pd

constructors = pd.read_csv(r"C:\Users\vinee\Desktop\Github\Formula1\dataset\constructors.csv")
circuits = pd.read_csv(r"C:\Users\vinee\Desktop\Github\Formula1\dataset\circuits_2.csv")
results = pd.read_csv(r"C:\Users\vinee\Desktop\Github\Formula1\dataset\results.csv")
drivers = pd.read_csv(r"C:\Users\vinee\Desktop\Github\Formula1\dataset\drivers.csv")
races = pd.read_csv(r"C:\Users\vinee\Desktop\Github\Formula1\dataset\races.csv")


print(constructors)
print(races)
print(circuits)
print(results)
print(drivers)
