import pandas as pd

def centimetrosAPulgadas(cm):
    return cm / 2.54

# Leer el archivo Excel
df = pd.read_csv("mueblesMedidas.csv")

# Añadir una columna al DataFrame que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Pulgadas"] = df["Centrímetros"].apply(centimetrosAPulgadas)

df.to_csv("muebleMedidasConvertidas.csv", index=False)

print("Conversión compeltada y guardada en una archivo llamado 'muebleMedidasConvertidas.csv'")