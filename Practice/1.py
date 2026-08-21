def calculator(*numbers):
    sum = 0
    subtract = 0
    multiplication = 1
    for number in numbers:
        sum = sum + number
        subtract = subtract - number
        multiplication = multiplication * number
    return sum, subtract, multiplication
print(calculator(1,2,3,4,5))
print(calculator(1,2,3,4,5,6,7,8,9,10))


def best_in_python(**python):
    sum = 0
    for division, count, in python.items():
        print(division, "=", count)
        sum = sum + count
    avg = sum/len(python)
    return avg
print(best_in_python(A=30, B=20, C=42, D=32, E=24, F=30, G=21))


def deco(func):
    def interview(name):
        print("Good Morning")
        func(name)
        print("Thank you, have a nice day.")
    return interview

@deco
def greeting(name):
    print(f"I am {name}. I want to be software engineer")
greeting("Deevesh")