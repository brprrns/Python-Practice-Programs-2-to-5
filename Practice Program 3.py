numbers = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

unique_numbers = []
seen = set()

for number in numbers:
    if number not in seen:
        unique_numbers.append(number)
        seen.add(number)

print(unique_numbers)