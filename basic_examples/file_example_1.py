# path = "C:\\Users\\Stuart\\GitHub\\curious-about-coding-03-file-io\\example_data\\one_column_data.csv"

path = r"C:\Users\Stuart\GitHub\curious-about-coding-03-file-io\example_data\one_column_data.csv"

# read a file with readline

f = open(path, mode="r")

keep_reading = True

while keep_reading:

    line = f.readline()

    if line == "":
        keep_reading = False
    else:
        print(line)

f.close()

# read a file looping over the lines

f = open(path, mode="r")

for line in f:
    line = line.strip()
    print(line)

f.close()

# loop over file and store lines in a list (memory inefficient)

f = open(path, mode="r")

lines = []

for line in f:
    line = line.strip()
    lines.append(line)

for line in lines:
    print(line)

# read a file with readlines (memory inefficient)

f = open(path, mode="r")

# reads all the lines
lines = f.readlines()

for line in lines:
    line = line.strip()
    print(line)

f.close()
