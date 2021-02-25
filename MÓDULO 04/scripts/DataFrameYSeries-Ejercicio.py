import pandas as pd

list_numero = [10,20,10]
numeros = pd.Series(list_numero)

list_color = ['rojo','verde','azul']
colores = pd.Series(list_color)

df = pd.DataFrame()

df['Numero'] = list_numero
df['Color'] = list_color

avengers = pd.read_csv('./data/pandas/avengers.csv')
print(avengers.head())

print(avengers.head(10))

print(avengers.tail())
print()
print(avengers.shape)