from sympy import divisor_count

count = 0
primo = 1

while True:
    if divisor_count(primo) == 2:
        print(primo)
    primo += 1
    if count <= 1024:
        count += 1
    else:
        break
    
    
    
    
