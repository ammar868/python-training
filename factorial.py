def factorial(n:int):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)

def list_factorial(numbers: list[int]):
    return [factorial(n) for n in numbers]