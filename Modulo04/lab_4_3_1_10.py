'''
Descripción: Convirtiendo el consumo de combustible
Autor: Daniel Almendariz
Fecha: 06 oct 2022
'''
 #se calcula cuanta gasolina es que se utiiliza 
def l100kmtompg(litros):
    galones = litros / 3.785411784
    millas = 100 * 1000 / 1609.344
    return millas / galones
    
#se calcula cuaas seran las millas para poder imprimir cuntas millas por galon se necesitan
def mpgtol100km(millas):
    km100 = millas * 1609.344 / 1000 / 100
    litros = 3.785411784
    return litros / km100


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))