for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

#pattern
for x in range(5):
    print(" * " *x )

# F symbol
print("\n\n\n\n\n")
numbers = [5,2,5,2,2]
for y in numbers:
    print("X" * y)

#second menthod
print("\n\n\n\n\n")
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)