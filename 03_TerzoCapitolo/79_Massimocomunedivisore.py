print("inserisci due numeri")

m =int(input())
n =int(input())

if m < n:
    d = m
else:
    d = n
    

while m % d != 0 or n % d != 0:
    d = d-1
    
    
    
print(d)