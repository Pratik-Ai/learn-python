try:
    age = int(input("age :  "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print('invalid statement')
except ZeroDivisionError:
    print('not divisible by zero')