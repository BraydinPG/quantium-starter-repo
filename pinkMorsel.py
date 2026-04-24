import pandas as pd
import glob

files = sorted(glob.glob('quantium-starter-repo/data/daily_sales_data_*.csv'))

# Load data
df_list = [pd.read_csv(files) for files in files]
df = pd.concat(df_list, ignore_index=False)

# Transform data
df['price'] = df['price'].str.replace('$','', regex=False)
df['price'] = pd.to_numeric(df['price'], errors='coerce')
df['sales'] = df['price'] * df['quantity']

# Filter data
pinkMorsel_df = df[df['product']=='pink morsel'][['sales', 'date', 'region']].reset_index(drop=True)
print(pinkMorsel_df.head(n=15))

# Convert new table to CSV

pinkMorsel_df.to_csv('pinkMorsel_sales.csv', index=False)