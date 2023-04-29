import json

# Define some data to be written to the JSON file
classification = {
    "key": ["account", "user", "system", "application",'password'],
    "issue": ["locked", "unlocked", "reset", "connection", "access","reset"],
    "ci": ["vcn",'sap','adobe','teams']
}

# Specify the file name and location
filename = "data.json"

# Open the file in write mode and write the data to it
with open(filename, "w") as f:
    json.dump(classification, f)
