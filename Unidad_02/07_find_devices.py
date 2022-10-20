file = open("devices.txt", "r")

line = input("Que dispositvo necesitas? ")

for line in file:
    line = line.strip()
    
    if "Switch" in line: 
        print(line)
        
    else:
        print("Dispositivo no encotrado :(") 

file.close()