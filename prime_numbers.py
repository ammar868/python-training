def is_prime(n: int):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3 , n//2 + 1):
        if n % i ==0: 
            return False
    return True

x = int(input("please enter a number "))

counter = 0 

for i in range(2,x+1):
    if is_prime(i):
        counter + 1

print(counter)



