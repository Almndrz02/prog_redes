from curses import init_pair


file = open("devices.txt", "a")

while True: 
    nuevo = input("Que dispositivo quieres agregar? ")
    
    if nuevo == 'exit':
        break
    file.write(nuevo+"\n")
    
    print ('')
    file.close()



