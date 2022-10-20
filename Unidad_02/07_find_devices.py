file = open("devices.txt", "r")

dispositivo = input("Que dispositvo necesitas? ")
fal = False


for line in file:
    line = line.strip()
    
    if dispositivo in line and len(dispositivo)>3:
        fal = True
        print(line)
        
if fal == False:
    print("Dispositivo no encontrado")
        

file.close()