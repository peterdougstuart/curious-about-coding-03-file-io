from os.path import dirname, join

path = join(
    dirname(dirname(__file__)),
    "example_data",
    "example.csv",
)

f = open(path, mode="w")

f.write("Name, Team\n")
f.write("Peter, Aston Villa\n")
f.write("Abdi, Chelsea\n")
f.write("Gaurav, Watford\n")
f.write("Sarah, Arsenal\n")
f.write("Stephen, Real Bedford\n")

f.close()
