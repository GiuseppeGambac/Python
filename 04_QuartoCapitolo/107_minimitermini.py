def Minimitermini(nominatore,denominatore):
        
    if nominatore < denominatore:
          d = nominatore
    else:
           d = denominatore
        

    while nominatore % d != 0 or denominatore % d != 0:
      d = d-1
  
    return nominatore/d,denominatore/d





print(Minimitermini(5,20))
    

    
    
    