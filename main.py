import keyboard

with open("texto.txt","a") as archivo:
    letras =keyboard.record(until="esc")
    for l in letras:
        if l.event_type =="down": 
            if l.name=="space":
                archivo.write(" ")
            elif l.name=="enter":
                archivo.write(" \n")
            elif len(l.name)==1:
                archivo.write(l.name)
            
                
  


     



    

             
             
             
             
    
    