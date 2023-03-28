import sys
import pandas as pd


input_excel = sys.argv[1]

# Reading the csv file content from NiFi
csv_df = pd.read_excel(input_excel)
  
# send excel file back to NiFi
csv_df.to_csv(sys.stdout.buffer, index=False)