import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = r'C:\Users\Lenovo\Desktop\ai-model\monatszahlen2405_verkehrsunfaelle_export_31_05_24_r.csv'
data = pd.read_csv(url)

# Display the first few rows of the dataset
data.head()

# Filter out records after 2020
data = data[data['JAHR'] <= 2020]

# Display the first few rows after filtering
data.head()

