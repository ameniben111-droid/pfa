import pandas as pd

data ={
    'ID': [101, 102, 103],
    'Prix': [15.0, 25.0, 10.0],
    'Quantite':[3, 2, 5],
    'Remise': [10, 5, 0]
}

df = pd.DataFrame(data)

df.to_csv('ventes.csv', index=False)

print("le fichier 'ventes.csv' a été généré avec succès !")