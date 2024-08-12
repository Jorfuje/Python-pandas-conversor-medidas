import pandas as pd

# Dataframe es la información básica con el nombre de las piezas y centímetros para poder armar el Excel

data = {
    "piezas": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral" ],
    "Centrímetros": [40, 120, 60, 30, 180]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_csv("mueblesMedidas.csv", index=False)
