'''
Descripción: La sentencia continue - El Bonito Devorador de Vocales
Autor: Daniel Almendariz
Fecha: 29 sep 2022
'''

word_witchot_vowels = ""

user_word = input ("Input your word: ").upper()

for letter in user_word:
    if letter == 'A':
        continue 
    elif letter == 'E':
        continue 
    elif letter == 'I':
        continue 
    elif letter == 'U':
        continue 
    elif letter == 'O':
        continue
    else :
        word_witchot_vowels += letter
        
print(word_witchot_vowels)