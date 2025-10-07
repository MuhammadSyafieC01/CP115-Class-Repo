score_input = input()

# TODO: Your code here
passing_count = 0
failing_count = 0
total = 0
while score_input != "end":
    score_input = int(score_input)

    if score_input >= 60:
        passing_count = passing_count + 1
        print("Pass")
    else:
        failing_count = failing_count + 1
        print("Fail")
    total += 1
    score_input = input()

pass_rate = passing_count / total

print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
