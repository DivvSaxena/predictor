import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = r"C:/Users/Lenovo/Desktop/predictor/monatszahlen2405_verkehrsunfaelle_export_31_05_24_r.csv"
data = pd.read_csv(url)

# Assuming your column names are 'Category', 'Accident-type', 'JAHR', 'MONAT', and 'WERT'
selected_columns = ['MONATSZAHL', 'AUSPRAEGUNG', 'JAHR', 'MONAT', 'WERT']  # Adjust column names if needed

# Select the first 5 columns
data = data[selected_columns]

# Display the first few rows of the dataset
data.head()

# Filter out records after 2020
data = data[data['JAHR'] <= 2020]

# Display the first few rows after filtering
data.head()

print(data.head())

