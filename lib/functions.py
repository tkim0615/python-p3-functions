#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
print(greet_programmer())

def greet(name):
    print(f"Hello, {name}!")
print(greet("Naureen"))



def greet_with_default(name="programmer"):
    print(f'Hello, {name}!')

print(greet_with_default())

def add(num1, num2):
    return num1 + num2

sum = add(1,2)
print(sum)

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    else:
        return number / 2

result = halve(10.5)
print(result)