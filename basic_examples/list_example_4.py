# python has inbuilt functions to calculate statistics of a list

cost_breakdown = [100.0, 200.0, 50.0, 60.0, 205.0]


print("Sum", sum(cost_breakdown))
print("Min", min(cost_breakdown))
print("Max", max(cost_breakdown))
print("Len", len(cost_breakdown))

# we can calculate the average by dividing the sum by the length
print(sum(cost_breakdown) / len(cost_breakdown))
