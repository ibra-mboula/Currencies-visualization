from django.shortcuts import render,HttpResponse

# La vu est cree pour retourner un template

def stocks(request):
    # la fonction render va nous retourner notre template, on lui passe
    # la requete de l'utilisateur et le chemin vers le html
    return render (request,  "myStocks/index.html", context= {"liste" : range(10)})


