# pip install pandas
import pandas as pd

#lendo o arquivo CSV diretamente da URL e armazenando em um DataFrame
df = pd.read_csv ("https://raw.githubusercontent.com/nataliavalentin/base-cervejas/master/Heineken_Consumo_aula.csv")

#mostra informações sobre o DataFrame, como número de linhas, colunas, tipos de dados e valores nulos
df.info()

#mostra as 5 primeiras linhas do DataFrame
print(df.sample(5))

#Corrigindo os nomes das colunas
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace("(", "")
df.columns = df.columns.str.replace(")", "")

#verifica se há valores nulos no DataFrame e retorna True se houver algum valor nulo, caso contrário retorna False
df.isnull().values.any()

#remove as linhas com valores nulos do DataFrame, caso haja algum valor nulo
df.dropna(how='any',inplace=True)

#troca a virgula por ponto e converte a coluna para o tipo float
df['Temperatura_Media_C'] = df['Temperatura_Media_C'].astype(str).str.replace(',','.').astype(float)
df['Temperatura_Minima'] = df['Temperatura_Minima_C'].astype(str).str.replace(',','.').astype(float)
df['Temperatura_Maxima_C'] = df['Temperatura_Maxima_C'].astype(str).str.replace(',','.').astype(float)
df['Precipitacao_mm'] = df['Precipitacao_mm'].astype(str).str.replace(',','.').astype(float)

df.duplicated()

df.drop_duplicates()

df.describe()


#GRAFICOS:

# import plotly.express as px
# import plotly.graph_objects as go
# import matplotlib.pyplot as plt
# import seaborn as sns

# dias_semana = sum(df[df.Final_de_Semana == 0] ['Consumo_de_cerveja_litros'])
# finais_semana = sum(df[df.Final_de_Semana == 1] ['Consumo_de_cerveja_litros'])

# labels = ['Dias de semana', 'Final de semana']
# values = [dias_semana, finais_semana]

# fig = go.Figure(data=[go.Bar(x=labels, y=values, marker_color='crimson')])
# fig.show()

#cria coluna dia da semana
df['dia_semana'] = pd.to_numeric(df['Data'].dt.day_of_week)

# consumo_dia_semana = df.groupby(by = 'dia_semana', as_index=False)['Consumo_de_cerveja_litros'].sum()
# consumo_dia_semana.dia_semana = consumo_dia_semana.dia_semana.map({0: 'Segunda-feira', 1: 'Terça-feira', 2: 'Quarta-feira', 3: 'Quinta-feira', 4: 'Sexta-feira', 5: 'Sábado', 6: 'Domingo'})
# cores = [  "#F8C8DC",  "#BDE0FE",  "#CDEAC0",  "#FFF1B6",  "#FFD6BA",  "#DCC6E0",  "#D6E2E9"]

# fig, axes = plt.subplots()
# axes.bar(x = consumo_dia_semana.dia_semana.values, height=consumo_dia_semana.Consumo_de_cerveja_litros.values, color = cores)

# axes.set_title("Consumo de cerveja por dia da semana")
# plt.show()

#FAZER GRAFICO DE PIZZA COM O CONSUMO DE CERVEJA POR DIA DA SEMANA