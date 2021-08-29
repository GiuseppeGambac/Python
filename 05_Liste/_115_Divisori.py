def divisori (numero):
    numeri = []
    
    for i in range (1, numero):
      
      if numero % i == 0:
        numeri.append(i)
    return numeri


if __name__ == '__main__':

   print(divisori(80))
        
        
        
        
