total = ''
contador_notas = 0 

import sys
while contador_notas <= 10:
    
    z = input("Place your grade:")
    x = int(contador_notas) + int(z)
    finalGrade = int(z)

    try:
        if finalGrade != int:
            print()

    except ValueError:
        print("please provide a number!")
    
    mediaTurma = x/10
    break
try:
    print(mediaTurma)
except ValueError:
    print("please provide a number")