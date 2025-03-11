path = r"C:\Users\Stuart\GitHub\curious-about-coding-03-file-io\example_data\santas_nice_list.csv"

# Read the file into memory
file_handler = open(path, mode="r")

keep_reading = True
data = []

while keep_reading:

    line = file_handler.readline()

    if line == "":
        keep_reading = False
    else:
        data.append(line)

file_handler.close()

louis_on_nice_list = False

# Check if Louis is on the nice list

for line in data:
    if "Louis" in line:
        louis_on_nice_list = True

if louis_on_nice_list:
    print("Louis is on the nice list")
else:
    print("Sorry Louis, you are not on the nice list")
