#Pelusi Matteo 3M

#Es 1

filename='Voti.txt'
x=float(0)
y=float(0)
with open(filename) as file:
    for line in file:
        voti=float(line.rstrip())
        print("voto:",voti)
        x=x+voti
        y=y+1
media=x/y
print("La media degli alunni è:",media,)

#Es 2

voti = []
file = "Voti.txt"
with open(file) as file:
    i = 0
    for line in file:
        voto = float(line.strip()) 
        voti.append(voto)
somma = 0 
for voto in voti:
    somma += voto
media = somma / len(voti)
print("Voti degli studenti:")
for voto in voti:
    print(voto, end=" ")
print("Media dei voti:", media)