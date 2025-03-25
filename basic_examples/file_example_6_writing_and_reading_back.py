from os.path import dirname, join

example_data_path = join(
    dirname(dirname(__file__)),
    "example_data",
    "example.csv",
)


f = open(example_data_path, mode="w")

f.write("Name, Team\n")
f.write("Peter, Aston Villa\n")
f.write("Abdi, Chelsea\n")
f.write("Gaurav, Watford\n")
f.write("Sarah, Arsenal\n")
f.write("Stephen, Real Bedford\n")

f.close()

# read file back

f = open(example_data_path, mode="r")


headers = f.readline().strip().split(",")

headers = [header.strip() for header in headers]

# read data

rows = []

for line in f:

    row_data = line.strip().split(",")
    row_data = [data.strip() for data in row_data]

    row_dict = {}

    for i, header in enumerate(headers):
        row_dict[header] = row_data[i]

    rows.append(row_dict)

print(rows[0]["Name"])
