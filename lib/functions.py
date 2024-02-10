#!/usr/bin/env python3
def greet_programmer():
   print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")



def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")

def add(num1, num2):
    sum_result = num1 + num2
    return sum_result

result = add(1, 2)
print(result)

def halve(number):
    if type(number) in (int, float):
        return number / 2
    else:
        return None

result = halve(4)
print(result)

result = halve("two")
print(result)

