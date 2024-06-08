import pandas as pd

# Cargar el conjunto de datos con el delimitador correcto
data = pd.read_csv('data.csv', delimiter=';')

# Mostrar información general del dataset
print(data.info())

# Ver las primeras filas del dataset
print(data.head())

# Verificar si hay valores nulos
print(data.isnull().sum())

# Ver la distribución de la variable objetivo
#print(data['Target'].value_counts())
