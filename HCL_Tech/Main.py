import pandas as pd
import json

# Reading the excel file.
df = pd.read_excel("HCL_Tech/test_data.xlsx")

# loading the json file
filename = 'HCL_Tech/data.json'
with open(filename, "r") as f:
    classification = json.load(f)

# Create empty lists for each column
key_list = []
issue_list = []
ci_list = []

# Loop through each row in the dataframe
for index, row in df.iterrows():
    # Split the string into a list of words
    words = row['Summary'].split()
    # Initialize variables for key, issue, and ci
    key = ''
    issue = ''
    ci = ''
    # Loop through each word in the list
    for word in words:
        # Check if the word is in 'key' and assign it to the key variable
        if word.lower() in classification["key"]:
            key = word
        # Check if the word is in 'issue' and assign to the issue variable
        elif word.lower() in  classification["issue"]:
            issue = word
        # Check if the word is 'ci' and assign to the ci variable
        elif word.lower()in classification["ci"]:
            ci = word
        if key == '' and issue=="" and ci== "":
            issue = "Anonymous data"
    # Append the values to the corresponding lists
    key_list.append(key)
    issue_list.append(issue)
    ci_list.append(ci)

# Create the final dataframe with the three columns
final_df = pd.DataFrame({'key': key_list, 'issue': issue_list, 'ci': ci_list})
final_df['Summary']=df['Summary'] 

# saving the file into csv format
final_df.to_csv("final_data.csv", index=False)


# Print the final dataframe
# print(final_df)