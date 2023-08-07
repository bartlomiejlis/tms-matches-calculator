#Kalkulator ilości dopasowań z pamięci tłumaczeniowych
import json
gvn_jsonfile = open("Analysis #1.json")
json_data = json.load(gvn_jsonfile)

#Główny skrypt programu
def main():
    print("Kalkulator ilości dopasowań z pamięci tłumaczeniowych \n")

    #Informacja o numerze zlecenia
    project_name = json_data["projectName"]
    print("Numer zlecenia:", project_name)

    #Informacja o języku źródłowym i docelowym tłumaczenia
    source_lang = json_data["analyseLanguageParts"][0]["sourceLang"]
    target_lang = json_data["analyseLanguageParts"][0]["targetLang"]
    print("Para językowa:", source_lang, "->", target_lang)

    #Obliczanie ilości dopasowań z pamięci tłumaczeniowych. Za minimalną wartość dopasowania przyjęto 70%.
    tm_pages1 = json_data["analyseLanguageParts"][0]["data"]["contextMatch"]["normalizedPages"]
    tm_pages2 = json_data["analyseLanguageParts"][0]["data"]["match100"]["normalizedPages"]["tm"]
    tm_pages3 = json_data["analyseLanguageParts"][0]["data"]["match95"]["normalizedPages"]["tm"]
    tm_pages4 = json_data["analyseLanguageParts"][0]["data"]["match85"]["normalizedPages"]["tm"]
    tm_pages5 = json_data["analyseLanguageParts"][0]["data"]["match75"]["normalizedPages"]["tm"]
    all_tm_pages = tm_pages1 + tm_pages2 + tm_pages3 + tm_pages4 + tm_pages5
    all_pages = json_data["analyseLanguageParts"][0]["data"]["total"]["normalizedPages"]
    tm_ratio = all_tm_pages / all_pages
    print("Liczba stron (1800 zzs): " + "%.2f" % all_tm_pages) #Wynik w liczbach stron rozliczeniowych 1800 zzs
    print("TMs matches: " + "{0:.0%}".format(tm_ratio)) #Wynik w %

    wait = input()
    
main()