from os.path import dirname, join

path = join(
    dirname(dirname(__file__)),
    "example_data",
    "santas_nice_list.csv",
)

file_handler = open(path, mode="r")

keep_reading = True

while keep_reading:

    line = file_handler.readline()

    if line == "":
        keep_reading = False
        print("Sorry Louis, you are not on the nice list")
    else:
        if "Louis" in line:
            keep_reading = False
            print("Louis is on the nice list")

file_handler.close()
