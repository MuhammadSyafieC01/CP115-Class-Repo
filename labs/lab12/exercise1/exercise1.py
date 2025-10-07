price = float(input())

# TODO: Your code here
item_count = 0
total_cost = 0

while price != -1:
    item_count += 1 
    total_cost += price 
    price = int(input("Enter item prices or -1 to stop:"))

print(item_count)
print(f"{total_cost:.2f}")
