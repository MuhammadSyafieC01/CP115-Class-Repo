age_input = input()

# TODO: Your code here
age_count = 0
total_age = 0

while age_input != "done":
    age_input=int(age_input)
    age_count += 1
    total_age += age_input
    age_input = input()

average_age = total_age / age_count

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
