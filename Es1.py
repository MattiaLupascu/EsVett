import numpy as np

#ES_1

voti_testo="file.txt"
voti_array=np.zeros(10)
with open(voti_testo) as file:
    i=0
    for linea in file:
        voti_array[i]=float(linea.rstrip())
        i=i+1

media=0
for i in range(10):
    media=voti_array[i]+media
print(media/10)

#ES_2

voti_testo="file.txt"
voti_lista=[]
with open(voti_testo) as file:
    for linea in file:
        voti_lista.append(int(linea.rstrip()))
media=0
for i in range(10):
    media=voti_lista[i]+media
print(media/10)





