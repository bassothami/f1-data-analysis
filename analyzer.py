import pandas as pd
import numpy as np

#encapsula todas as análises da F1
class Analysis:
    def __init__(self, df):
        self.df = df

    #agrupa por ponto de pilotos e ordena do maior para menor
    def ranking(self):
        return self.df.groupby("Piloto")["Pontos"].sum().sort_values(ascending=False)
    
    #agrupa por piloto e posicao, retornando a média
    def mean_position(self):
        return self.df.groupby("Piloto")["Posicao"].mean()
    
    #agrupa por piloto e posicao, aplicando std para retornar consistencia
    def consistency(self):
        return self.df.groupby("Piloto")["Posicao"].apply(np.std)
    
    #baixo valor = consistente
    #alto valor = irregular