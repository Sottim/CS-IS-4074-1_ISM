import pandas as pd

# Read existing CSV
df = pd.read_csv('/home/KutumLabGPU/Documents/santosh/capstone_project/models/WSIDimension/data-path.csv')

# Add MPP and magnification columns
df['slide_mpp'] = 0.25
df['magnification'] = 40.0

# Save the modified CSV
df.to_csv('/home/KutumLabGPU/Documents/santosh/capstone_project/models/WSIDimension/data-path-with-meta.csv', index=False)
