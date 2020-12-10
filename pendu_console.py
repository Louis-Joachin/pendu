# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:14:09 2020

@author: louis
"""
from random import choice
from tkinter import Tk
import unicodedata

def MotAleatoire(): #Fonction générant le mot
    fich=open('mots.txt','r') #Ouverture du fichier
    l=fich.readlines() #extraction des données
    fich.close() #fermeture du fichier
    mot=""
    while len(mot)<4:
        mot=choice(l)
        mot=mot.strip("\n")
    mot=mot.lower()
    mot=''.join((c for c in unicodedata.normalize('NFD', mot) if unicodedata.category(c) != 'Mn'))
    print(mot)
    return(mot)
    


def Affichage(erreur): #Fonction affichage avec les différents stade du pendu
    if erreur == 0:
        print("")
        print("    ")
        print("    ")
        print("    ")
        print("    ")
        print("")
        print("---------")
    if erreur == 1:
        print("")
        print("|    ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|")
        print("---------")
    if erreur == 2:
        print("______")
        print("|    ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|")
        print("---------")
    if erreur == 3:
        print("______")
        print("|/    ")
        print("|     ")
        print("|     ")
        print("|     ")
        print("|")
        print("---------")
    if erreur == 4:
        print("______")
        print("|/   |")
        print("|    O")
        print("|    ")
        print("|    ")
        print("|")
        print("---------")
    if erreur == 5 :
        print("______")
        print("|/   |")
        print("|    O")
        print("|   /| ")
        print("|    ")
        print("|")
        print("---------")
    if erreur == 6 : 
        print("______")
        print("|/   |")
        print("|    O")
        print("|   /|\ ")
        print("|    ")
        print("|")
        print("---------")
    if erreur == 7:
        print("______")
        print("|/   |")
        print("|    O")
        print("|   /|\ ")
        print("|   /  ")
        print("|")
        print("---------")
    if erreur == 8:
        print("______")
        print("|/   |")
        print("|    O")
        print("|   /|\ ")
        print("|   / \ ")
        print("|")
        print("---------")
        
def Pendu(score=0):
    vie=8 #initialisation du nombre de vie restante
    mot=MotAleatoire() #mot aléatoire
    resultat=mot[0] # initialisation du mot a deviner
    for i in range(len(mot)-1):
        resultat+="_" #création des underscores
    while vie != 0 and "_" in resultat: #continuer le jeu tant que le joueur a trouvé ou qu'il a encore des vies
        Affichage(8-vie) # affichage du pendu
        print(resultat) #affichage des lettres trouvées
        print("Il vous reste",vie,"essais") #affichage du nombre de vies
        essai=input("Veuillez entrer une lettre : ") #on demande la lettre
        if essai not in mot: #si c'est faux
            vie-=1 #on enlève une vie
            print ("La lettre n'était pas dans le mot. Vous perdez une vie.") 
        else: #si c'est juste
            if essai in resultat[1:]: 
                print ("Lettre déja entrée. Rééssayez")
            else:
                index = 1
                for lettre in mot[1:]:
                    if lettre == essai:
                        resultat=resultat[:index]+lettre+resultat[index+1:]
                    index+=1
                print("Lettre trouvée. Continuez")
    if vie == 0:
        print("Vous avez perdu")
        print("Vous avez obtenu un score de  : ",score)
    else:
        print("Félicitation, vous avez gagné !")
        a=input("Rejouer ? [O/N]  :    ")
        while a not in ['O','N','o','n']:
            a=input("Réponse non valide. Rejouer ? [O/N]  :    ")
        if a == 'O' or a == 'o':
            Pendu(score+vie)
        elif a == 'N' or a == 'n':
            print("Merci d'avoir joué ! Score Final : ",score+vie)
        
Pendu()
        
        
        


            
            
        
