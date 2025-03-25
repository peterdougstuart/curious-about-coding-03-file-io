from os.path import dirname, join

current_dir = dirname(__file__)
parent_dir = dirname(current_dir)
example_data_dir = join(parent_dir, "example_data")
example_data_path = join(example_data_dir, "santas_nice_list.csv")

print(__file__)
print(current_dir)
print(parent_dir)
print(example_data_dir)
print(example_data_path)
