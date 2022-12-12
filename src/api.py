from pprint import pprint
from datetime import timedelta, date

import requests


# days = 30 pour les 30 dernier jours
# Function qui return les jours et les devises

def getData(currencies, days=30):
    
    _today = date.today()
    start_day = _today - timedelta(days=days)

    # f pour tout convertir en string
    # {','.join(currencies)} c'est pour avoir une list de dévise séparé par des virgules car l'adresse de base est :
    # https://api.exchangerate.host/timeseries?start_date=2021-12-31&end_date=2022-6-04&symbols=USD,EUR

    symbols = ','.join(currencies)
    requete = f"https://api.exchangerate.host/timeseries?start_date={start_day}&end_date={_today}&symbols={symbols}"
    req = requests.get(requete)

    # récupération des valeurs associées à la clé rates voir screen thunder
    # req.json() read tout le fichier json , get("read le contenu de rates")
    api_rates = req.json().get("rates")

    #Il faut recuperer la valeur de chques devise et l'associer à notre dictionnaire all_rate
    # pour chaques devise on cree des clés >> 'devise' : [] on va la remplir plustard ligne 50 for each_day

    # comprehension de dictionnaire
    #all_data = {currency: [] for currency in currencies} # on cree un dictionaire avec des clé(depends du nbre de devise)

    #creation de dictionnaire currencies vident pour  meilleur exploitation des data
    all_data = dict()
    for currency in currencies :
        all_data[currency]=[]
        #pprint(all_data) # {'CAD': [], 'USD': []}

 
    #pprint(all_data) # {'USD': []}    {'USD': [] , 'EUR': []}

    #recuperer la clé de tous les jours  que je classe avec sorted
    all_days = sorted(api_rates.keys())
    #pprint(all_days) #['2022-10-30',
                      #'2022-10-31'....]

    # on recupére pour chaques jours les valeurs de devise
    # pour associer les valeurs de chques devise à notre dictionnaire all_rate

    for each_day in all_days:

        #pour récuperer la valeur que j'ai chaques jours
        #pprint(api_rates.get(each_day).values()) >>> dict_values([1.55472, 0.995269])

        #print(api_rates.get(each_day))  # {'AUD': 1.354604, 'USD': 0.995269}
                                        # {'AUD': 1.345788, 'USD': 0.987847}

        # En fesant .append je viens remplir mon dictionnaire avec la valeur d'une items chaques jours

        # for [('AUD', 1.55472)] in dict_items([('AUD', 1.55472)]) >>  1.55472
        # .value() aurait pu etre utiliser mais ne me permet pas de recuperer les valeures de plusieurs devises
        #currency = keys    rate = value
        for currency, rate in api_rates.get(each_day).items() :

            # on vient remplir le dictionnaire vide déclaré plus haut
            #{'AUD': [1.55472,1.542442,1.544268,...


            [all_data[currency].append(rate)] #on add toutes les value dans la keys currencies


        #print(all_data)


   # pprint(all_data)

    return all_days, all_data

# pour que cette condition ne soit pas exécuté lorsqu'on importe le module api
if __name__ == '__main__':
    #getData(currencies=["AUD","USD"])

   days, rates =  getData(currencies=["AUD", "USD","CAD"] ,  days=5)
   pprint(days)
   pprint(rates)

