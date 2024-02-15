'''import  numpy as np


array = np.random.rand(3, 3)

print("Array  3x3:\n", array)
'''

''''' EX 17
#crea un programma che somma  tutti gli elementi dentro array  numpy 
import numpy as np

array = np.array([[3, 6, 9],
                  [12, 15, 18],
                  [21, 24, 27]])

somma = np.sum(array)

# Stampiamo la somma
print("La somma", somma)
'''
''''''
#EX 18'
'''
import numpy as np

array = np.array([2, 6, 12, 5, 8, 10,44, 656,78,33])
calcolo_media = np.mean(array)
calcolo_mediana = np.median(array)
vrz = np.var(array)

print("Media array:",calcolo_media,"mediana:", calcolo_mediana,"varianza sarebbe:", vrz)
'''

#EX19
''''
import numpy as np



matrice_prima = np.array([[0, 1, 2]]) 
matrice_seconda = np.array([[3, 4, 5]])

risultato = matrice_prima * matrice_seconda

print("Matrice 1:\n", matrice_prima)
print("\nMatrice 2:\n", matrice_seconda)
print("\nRisultato della moltiplicazione elemento per elemento:\n", risultato)
'''
#EX20
''''
import numpy as np

sequenza_np = np.arange(10)

print("Sequenza :", sequenza_np)

''
#21
#utilizzo pandas
#('Nome', 'Età', 'Città') rappresentano i nomi delle colonne del DataFrame, mentre i valori associati a
# ciascuna chiave sono delle liste contenenti i dati corrispondenti per ciascuna colonna.
#'Nome': è una chiave del dizionario e il suo valore è una 
# lista di stringhe, rappresentanti i nomi delle persone.
#Ogni elemento della lista associata a una chiave rappresenta
# il dato corrispondente per una specifica colonna del DataFrame.
#ogni cosa che ce dentro la lista    e associata a una chiave cioe ex Nome   rappresenta
# la  colonna NOME  che sarebbe la CHIAVE mentre alice bo david sono i VALORI,lo stesso eta eta e chiave me ntre 23
#45 56 42 sono I VALORI associato alla chiave  ETA


import pandas as pd

dizionario_dati= {
    'Nome': ['Marco', ' Carlos', 'Caterina', 'Daniele'],
    'Età': [33, 55, 45, 40],
    'Città': ['Firenze', 'Milano', 'Palermo', 'Torino']
}

dataframe_d = pd.DataFrame(dizionario_dati)
print(dataframe_d)
'''
'''ex 22'''
''''
import pandas as pd

# Specifica il percorso del file CSV
percorso_file = "C:/Users/sandy/Desktop/fff.csv"

# Leggi il file CSV e caricalo in un DataFrame
df = pd.read_csv(percorso_file)

# Stampiamo le prime righe del DataFrame per verificarne il contenuto
print(df.head())
'''
'''EX23''''''
''''''''
import pandas as pd
Candidati={ "Nome": ["Sor","Laura","Maria","Cristhian"],
            "Età": [23,44,56,12],
            "Nazionalita":["Italiana","Araba","Cinese","Australiano"]}

df= pd.DataFrame(Candidati)
 #cosi mi stampa il nome colonna+ indice  
print("nome")
print('\n'.join(df['Nome']))
'''''

"ex 24"
'''''
import pandas as pd 

Artisti= { "Nome":["Michael "," Adele"," Vasco"],
        "Cognome": ["Jackson","Adkins","Rossi"],
        "eta":[65,32,55],
        "Genere musicale":["Pop Rock","Jazz","Rock"]}

df=pd.DataFrame(Artisti)

#filtra secondo una condizione

filtro= df[df["eta"] <60]
print("eta")
print(*filtro["eta"], sep="\n")

'''''
'ex 25'
''''
import pandas as pd

# Esempio di DataFrame
Valori = { "primo_valore": [1, 2, 3, 4, 5],
    'Secondo_valore': [5, 4, 3, 2, 1],
    "Terzo_Valore":[7,2,6,7,8]}

df = pd.DataFrame(Valori)
media = df.mean()
print(media)
print("Media di ogni colonna")
'''
"ex 26"
#Plot


import pandas as pd 
import matplotlib.pyplot as plt
date = pd.date_range(start="2022-01-01", end="2022-01-10")
valori = [1, 3, 5, 2, 4, 6, 8, 7, 9, 10]
dati_cronologici = pd.Series(valori, index=date)

# Crea il grafico a linee
plt.plot(dati_cronologici)

# Aggiungi etichette agli assi
plt.xlabel('Data')
plt.ylabel('Valore')

# Aggiungi titolo al grafico
plt.title('Grafico ')

# Mostra il grafico
plt.show()