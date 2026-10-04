import pandas as pd

print("HOLAAAAAA soyb polo")

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

print(df)
import pandas as pd

df = pd.read_csv("ventas.csv", parse_dates=["fecha"])

print(df.shape)          # filas y columnas
print(df.head())         # primeras filas
print(df.info())         # tipos de datos y nulos
print(df.describe())     # estadísticas

# Algunas cosas para practicar:
print(df.duplicated().sum())                         # duplicados
print(df.isna().sum())                               # nulos por columna
print(df.groupby("provincia")["total"].sum())        # ventas por provincia
print(df.groupby("categoria")["total"].mean())       # ticket promedio por categoría
print(df.groupby(df["fecha"].dt.year)["total"].sum())# ventas por año


print(df[df["total"] > 1000])                        # ventas mayores a 1000
