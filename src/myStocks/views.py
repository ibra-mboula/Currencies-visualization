from django.shortcuts import render,HttpResponse

import api

# La vu est cree pour retourner un template

def stocks(request):
    
    days, rates =  api.getData(currencies=["USD"], days=30)
    
    # la fonction render va nous retourner notre template, on lui passe
    # la requete de l'utilisateur et le chemin vers le html
    return render (request,  "myStocks/index.html", context= {"data" : rates["USD"], "days" : days })


