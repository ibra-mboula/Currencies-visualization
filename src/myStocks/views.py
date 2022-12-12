from django.shortcuts import render,HttpResponse

import api

# La vu est cree pour retourner un template

def stocks(request, ndays = 30 , ncurrencies = "LaDeviseVoulu"  ):
    
    # "USD".split(",")
    
    #Ici on recupère les data d'une devise du dictionnaire pendant ces 30 derniers jours
    days, rates =  api.getData(currencies = ncurrencies.split(","), days = ndays)
                                #currencies.split car getData va renvoyé une list hos ce qu'on veut dans notre url c'est une string
    
    
    # la fonction render va nous retourner notre template, on lui passe
    # la requete de l'utilisateur et le chemin vers le html, et les variables utilisés dans l'index
    
   #Dans ma variable data qui sera utilisé dans l'index on envoie tout le dictionnaire complet rates
    return render (request,  "myStocks/index.html", context= {"data" : rates, "days" : days })
                                                            
              
                                               
                                                #Ici on recupère les data d'une devise du dictionnaire pendant ces x jours             
                                                            #context= {"data" : rates["CAD"], "days" : days })
                                                             #Ici on à envoyé rate qui vient du dictionnaire 
                                                             #on avait en clé les dévises et leur valeur
                                                             #VU qu'on ne veut que les valeurs de USD on le met en crochet


