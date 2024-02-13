import pandas as pd
import numpy as np

df = pd.read_csv('data/maya-dev.tsv', delimiter='\t')
print(df)

# Find all unique "Change" tokens
print("Num unique labels = ", len(df.Change.unique()))
print("Unique labels: ")
print(df.Change.unique())

# Find all entries in the dataset where change type is TYPE:NEG

print(df[df.Change == 'TYPE:NEG'])