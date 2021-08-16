def calcoloprezzo(numeropezzi):
  
     if numeropezzi == 1:
         return 10.95
     elif numeropezzi ==0:
         return 0.0
     else:
         return (numeropezzi -1) *2.95 + 10.95


print(calcoloprezzo(2))