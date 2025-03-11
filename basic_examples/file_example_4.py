# Open a file and read its contents into a list

import os

# Determine the path to the example data file
script_dir = os.path.dirname(__file__)
repo_root = os.path.dirname(script_dir)
examples_dir = os.path.join(repo_root, "example_data")
example_file = os.path.join(examples_dir, "one_column_data.csv")

print("Loading data from:", example_file)

data = []

with open(example_file) as f:
    for line in f:
        data.append(line.strip())

for i in range(len(data)):
    print(data[i])
