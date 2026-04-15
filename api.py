import requests
import pandas as pd

def get_data():
    url = "https://api.jolpi.ca/ergast/f1/2023/results.json"

    response = requests.get(url)

    if response.status_code != 200:
        print("Erro na API:", response.status_code)
        return pd.DataFrame()

    data = response.json()

    #estruturas de armazenamento
    lista = []
    races = data['MRData']['RaceTable']['Races']

    for race in races:
        for result in race['Results']:
            lista.append({
                "Piloto": result['Driver']['familyName'],
                "Posicao": int(result['position']),
                "Pontos": float(result['points'])
            })

    #transforma lista em tabelas
    return pd.DataFrame(lista)