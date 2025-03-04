# we could use multiple variables instead of a list
# but this leads to more code and is less flexible

#  with multiple variables
print("With multiple variables")

cost_1 = 100.0
cost_2 = 200.0
cost_3 = 50.0
cost_4 = 60.0
cost_5 = 205.0

print(cost_1)
print(cost_2)
print(cost_3)
print(cost_4)
print(cost_5)

total = cost_1 + cost_2 + cost_3 + cost_4 + cost_5
print(total)

# with a list
print("With a list")

cost_breakdown = [100.0, 200.0, 50.0, 60.0, 205.0]
total = 0.0

for cost in cost_breakdown:
    print(cost)
    total += cost

print(total)
