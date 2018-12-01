class studente:
       def __init__(self,nome,cognome,classe):
             self.nome=nome
             self.cognome=cognome
             self.classe=classe


alunni = []
S=" "
n=input ("Quanti studenti vuoi inserire?")
n=int (n)
for a in range (n):
         nome=input ("Inserisci nome")
         cognome=input("inserisci cognome")
         classe=input("Inserisci classe")
         S=studente(nome,cognome,classe)
         alunni.append(S)
for alunno in alunni:
       print (alunno.nome)
       print(alunno.cognome)
       print(alunno.classe)                