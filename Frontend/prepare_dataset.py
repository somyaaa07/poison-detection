import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/tox_dataset_main.csv",
    encoding="latin1",
    skiprows=2
)

# Keep important columns
df = df[[
    'Toxin / Substance',
    'CNS Symptoms\n(at this phase)',
    'CVS Symptoms\n(at this phase)',
    'Respiratory Symptoms\n(at this phase)',
    'GI Symptoms\n(at this phase)',
    'Other / Systemic Symptoms\n(at this phase)',
    'Odour Present\n(optional parameter)'
]]

# Rename columns
df.columns = [
    'toxin',
    'cns',
    'cvs',
    'respiratory',
    'gi',
    'other',
    'odour'
]

# Remove empty rows
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/clean_toxic_dataset.csv", index=False)

print(" Dataset cleaned successfully!")
print(df.head())