numbers = [5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)

numbers.insert(0,10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.clear()
print(numbers)

numbers = [5, 2, 1, 5, 7, 4]
numbers.pop()
print(numbers)

print(numbers.index(5))
print(5 in numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)

print(numbers2)

