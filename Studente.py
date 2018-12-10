classi = []
classe Studente :
       def __init__ (self,nome,cognome,classe):
       self.nome = nome
       self.cognome = cognome
       self.classe =classe
 
 #main
 i=0
 num = input ("Quanti studenti ci sono ?")
 num = int (num)
 while i<num:
       nome = input ("inserisci il nome dello studente: ")
       cognome = input ("inserisci il cognome :")
       classe = input ("inserisci la classe: ")
       Studenti = Studente(nome,cognome,classe)
       classi.append (Sudenti)
       print (classi [i].nome, "//",classi[i].cognome,"//",classi[i].classe)
       i+=1
