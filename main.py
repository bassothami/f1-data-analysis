import pandas as pd
from api import get_data
from analyzer import Analysis

#pega dados da API
df = get_data()
analysis = Analysis(df)

#função de exibição
def show(title, series):
    print(title)
    print(series.sort_values(ascending=False).round(2).to_string())


#exibição das informações
show("\n RANKING DE PONTOS", analysis.ranking())
show("\n CONSISTÊNCIA", analysis.consistency())
show("\n POSIÇÃO MÉDIA", analysis.mean_position())


#exportação CSV
df_export = pd.DataFrame({
    "Pontos": analysis.ranking(),
    "Consistencia": analysis.consistency(),
    "Media_Posicao": analysis.mean_position()
}).round(2)

df_export.to_csv("resultado_f1.csv")

