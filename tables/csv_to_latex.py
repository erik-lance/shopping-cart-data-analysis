import pandas as pd

# Input filename by user
filename = input("Enter the filename: ")

# Read the CSV file
df = pd.read_csv(filename)

# Print file name
print("File name: ", filename)

# Print the dataframe
print(df)

# Convert the dataframe to LaTeX
print(df.to_latex(index=False))