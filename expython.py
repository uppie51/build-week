#def massimonumeri(a, b,c):
  #  return max(a,b,c)


# print(massimonumeri(10, 5, 8))

#ex2
#def Celsius_fahreheint(gradiCel):
  #  fahreheint=(gradiCel *9/5 )+32
   # return fahreheint
#gradiCel=float(input("inserisci i gradi in celsius per poi convertire in gradi Fahreheint: "))
#fahreheint=Celsius_fahreheint(gradiCel)
#print("i gradi in celsius", gradiCel, "corripondono a gradi in: " , fahreheint)

#ex3
#lista = [2,3,4,4, 3,1,2, 4, 3, 5]
#list_senza_duplicati = []

#for x in lista:
    #if x not in list_senza_duplicati:
       # list_senza_duplicati.append(x)
        #list_senza_duplicati.sort()

#print(list_senza_duplicati)


#ex4
#def palindromo(parola):
   # parola = parola.lower()  
    #lunghezza = len(parola)  
    
    

    #for i in range(lunghezza // 2):
        
        #if parola[i] != parola[lunghezza - 1 - i]:
          #  return False  
    #return True  

#parola=input("inserisci una parola:  ")
#if palindromo(parola):
 #    print("la prola e palindormo")
#else:
 #   print("non e palindromo")

#ex5
#def fattoriale_num(n):
   # if n == 0:
     #   return 1
   # else:
        #return n * fattoriale_num(n-1) #x se stesso n calcolando il fattoriale diminuendo
#n= int(input("Inserisci un numero: "))
#fattoriale = fattoriale_num(n)

#print("Il fattoriale di", n, "è:", fattoriale)

#ex6

#crea un dizionario da due liste una contiene chiavi altra valori
#un dizionario vuoto senza liste
#dizionario ={}
#creo prima lista chiavi
# listachiave= ["nome", 'età', 'altezza']
#creo seconda lista con valori
# listavalori = ['vanessa', 25, 1.84]
#cerco di mettere insieme le due liste con zip  creando una variabile 
# insiemechiave_valore = zip(listachiave, listavalori)
# aggiungo al dizionario vuoto questi due insiemi di valori

# #dizionario.update(insiemechiave_valore)
#print("Dizionario :", dizionario)

#Ex7
#def unisci_tuple(lista1, lista2):
   # list_tuple = []  
    #lunghezza = min(len(lista1), len(lista2)) 
    
    #for i in range(lunghezza):
       # list_tuple.append((lista1[i], lista2[i])) 

   # return list_tuple 
#list1 =["offerte di lavoro in: ","offerta di  lavoro in :" ,"offerta di lavoro in"]
#list2 = ["Gi group", "Randstad", "Adecco"]

#risultato = unisci_tuple(list1, list2)
#print("Lista di tuple :", risultato)

#Ex8

#lista_di_tuple = [("bingo", 3), ("bingo", 2), ("bingo", 1)]

#def secondo_elemento(tupla):
    #return tupla[1]

#lista_di_tuple.sort(key=secondo_elemento)

#print("Lista di tuple ordinata per il secondo elemento ovvero in modo ordinato :", lista_di_tuple)

#Ex9
#List comprehesion sarebbe lista= [x cosa for valore in range (0,100)]
 #1dafare valore aggiungere ala lista  ovvero x cosa = valore
 #2ciclo pvvero un ciclo, for 
#lista_priminum= [n**2 for n in range(0, 11)]

#print("Lista dei primi 10 numeri  quadrati  interi:", lista_priminum)


#Ex 10 
#lista = [1, 33, 45, 32,35,22,57,90, 55, 67, 98, 2]


#num_pari = [n for n in lista if n % 2 == 0]


#print("Numeri pari nella lista:", num_pari)

#ex11
#lista = ["ciao", "come", "stai", "laura", "cabello"]

#list_convert = [stringa.upper() for stringa in lista]

#print("Lista maiuscolo:",list_convert)

#EX12 
#lista_tuple = [(numero, numero**2) for numero in range(1, 30)]


#print("Lista di tuple (numero, quadrato del numero):", lista_tuple)

''' ex 13'''


'''list=[34,-23,33,-2,5]
lista_valorip=[ n for n in list if n>0]

print("Valori positivi nella lista:", lista_valorip)

'''
'''ex 14'''




'''lista_vocali = ["nadia", "atita", "baby", "enna"]

filtro = [parola for parola in lista_vocali if parola[0].lower() in 'aeiouAEIOU']

# Stampiamo la lista risultante con le parole che iniziano con una vocale
print("Parole che iniziano con una vocale:", filtro)
'''

'''EX 15'''

'''lista_alfa = ["abcdefghijklmnopqrstuvwxyz"]
alfabeto = [lettera for lettera in lista_alfa[0]]

print("Alfabeto:", alfabeto)
'''